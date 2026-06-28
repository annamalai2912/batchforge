import sqlite3

def fix_db():
    conn = sqlite3.connect('batchforge.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM scripts WHERE name='18_usb_device_history.bat'")
    row = cursor.fetchone()
    if row:
        script_id, content = row
        # The content has line continuations inside the double quotes
        new_content = content.replace(" |\n   Select-Object", " | Select-Object")
        new_content = new_content.replace(" |\n   Format-Table", " | Format-Table")
        
        # It had ^ characters as well. Let's do a more robust replacement.
        import re
        new_content = re.sub(r'\|\s*\^\s*\n\s*', '| ', new_content)
        new_content = re.sub(r"'\s*\|\s*\^\s*\n\s*", "' | ", new_content)
        
        cursor.execute("UPDATE scripts SET content=? WHERE id=?", (new_content, script_id))
        conn.commit()
        print("Fixed script in DB.")
    else:
        print("Script not found in DB.")
    conn.close()

if __name__ == "__main__":
    fix_db()
