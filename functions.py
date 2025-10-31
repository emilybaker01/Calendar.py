import sqlite3
con=sqlite3.connect('calendar.db')
cursor=con.cursor()

#create table
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS day(
        date INTEGER
        start_time INTEGER
        end_time INTEGER
        notes TEXT NOT NULL''')