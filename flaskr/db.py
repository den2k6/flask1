import sqlite3

DATABASE = "database.db"


def create_todos_table():
    """create table"""
    con = sqlite3.connect(DATABASE)
    con.execute(
        "CREATE TABLE IF NOT EXISTS todos (todo_id INTEGER, status TEXT, event TEXT, limits DATE)"
    )
    con.close()
