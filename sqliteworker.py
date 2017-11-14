import sqlite3

def addadminchatid():
    conn = sqlite3.connect('chat.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM chat')
    conn.commit()

