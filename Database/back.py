import sqlite3

def connect():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data (Id INTEGER PRIMARY KEY, date text, earnings integer, exercise text, study text, diet text, python text)")
    con.commit()
    con.close()

def insert(date, earnings, exercise, study, diet, python):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO data VALUES (NULL, ?,?,?,?,?,?)", (date, earnings, exercise, study, diet, python))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE id = ?", (id,) )
    con.commit()
    con.close()


def search(date = '', earnings = '', exercise = '', study = '', diet = '', python = ''):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data WHERE date = ? OR earnings = ? OR exercise = ? OR study = ? OR diet = ? OR python = ?", (date, earnings, exercise, study, diet, python))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

connect()