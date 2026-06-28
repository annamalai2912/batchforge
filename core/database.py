import sqlite3
import os
import sys

if getattr(sys, 'frozen', False):
    app_data = os.path.join(os.environ.get('APPDATA', ''), 'BatchForge')
    os.makedirs(app_data, exist_ok=True)
    DB_PATH = os.path.join(app_data, "batchforge.db")
else:
    DB_PATH = "batchforge.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS scripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT DEFAULT 'Uncategorized',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS script_tags (
            script_id INTEGER,
            tag_id INTEGER,
            PRIMARY KEY (script_id, tag_id),
            FOREIGN KEY(script_id) REFERENCES scripts(id) ON DELETE CASCADE,
            FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS run_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            script_id INTEGER,
            run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL,
            output TEXT,
            FOREIGN KEY(script_id) REFERENCES scripts(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            script_id INTEGER,
            trigger_type TEXT NOT NULL,
            trigger_time TEXT NOT NULL,
            FOREIGN KEY(script_id) REFERENCES scripts(id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
    ''')
    
    # Try to add category column if it doesn't exist (for existing DBs)
    try:
        cursor.execute("ALTER TABLE scripts ADD COLUMN category TEXT DEFAULT 'Uncategorized'")
    except sqlite3.OperationalError:
        pass
        
    # Insert default first_run setting if it doesn't exist
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('first_run', 'true')")
        
    conn.commit()
    conn.close()

def add_script(name, content, category="Uncategorized"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scripts (name, content, category) VALUES (?, ?, ?)", (name, content, category))
    conn.commit()
    script_id = cursor.lastrowid
    conn.close()
    return script_id

def get_all_scripts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category FROM scripts ORDER BY updated_at DESC")
    scripts = cursor.fetchall()
    conn.close()
    return scripts

def get_script(script_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, content, category FROM scripts WHERE id = ?", (script_id,))
    script = cursor.fetchone()
    conn.close()
    return script

def update_script(script_id, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE scripts SET content = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (content, script_id))
    conn.commit()
    conn.close()

def delete_script(script_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scripts WHERE id = ?", (script_id,))
    conn.commit()
    conn.close()

def delete_all_scripts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scripts")
    conn.commit()
    conn.close()

def get_setting(key, default_value=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else default_value

def set_setting(key, value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
