import sqlite3

def create_db():
    conn = sqlite3.connect('latecomers.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            parent_email TEXT NOT NULL,
            strikes INTEGER DEFAULT 0,
            fine INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_latecomer(name, email, parent_email):
    conn = sqlite3.connect('latecomers.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE email=?', (email,))
    student = c.fetchone()
    
    if student:
        strikes = student[4] + 1
        fine = 3000 if strikes >= 3 else 0
        c.execute('UPDATE students SET strikes=?, fine=? WHERE email=?', (strikes, fine, email))
    else:
        strikes = 1
        fine = 0
        c.execute('INSERT INTO students (name, email, parent_email, strikes, fine) VALUES (?, ?, ?, ?, ?)',
                  (name, email, parent_email, strikes, fine))
    
    conn.commit()
    conn.close()
    return strikes
