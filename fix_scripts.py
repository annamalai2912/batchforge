import sqlite3

def patch():
    conn = sqlite3.connect('batchforge.db')
    c = conn.cursor()
    c.execute('SELECT id, content FROM scripts')
    rows = c.fetchall()
    
    for row in rows:
        script_id = row[0]
        content = row[1]
        changed = False
        
        if '> software_list.txt' in content:
            content = content.replace('> software_list.txt', '> "%TEMP%\\software_list.txt"')
            if 'start notepad' not in content:
                content += '\nstart notepad "%TEMP%\\software_list.txt"'
            changed = True
            
        if '> drivers.txt' in content:
            content = content.replace('> drivers.txt', '> "%TEMP%\\drivers.txt"')
            if 'start notepad' not in content:
                content += '\nstart notepad "%TEMP%\\drivers.txt"'
            changed = True
            
        if changed:
            c.execute('UPDATE scripts SET content=? WHERE id=?', (content, script_id))
            print(f"Patched script ID {script_id}")
            
    conn.commit()
    conn.close()
    print('Patched DB successfully')

try:
    patch()
except Exception as e:
    print('Error:', e)
