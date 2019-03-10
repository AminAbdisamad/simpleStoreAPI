import sqlite3 as sqlite


class Database:
    connection = sqlite.connect("store.db")
    curser = connection.cursor()
    if __name__ == "__main__":
        createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text,password text)"
        curser.execute(createTable)
