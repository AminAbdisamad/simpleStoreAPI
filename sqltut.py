# from flaskext.mysql import MySQL
import sqlite3 as sqlite
# Database setup
# mysql = MySQL()
# mysql.init_app(app)
# app.config['MYSQL_DATABASE_USER'] = config.USERNAME
# app.config['MYSQL_DATABASE_PASSWORD'] = config.PASSWORD
# app.config['MYSQL_DATABASE_DB'] = config.DBNAME
# app.config['MYSQL_DATABASE_HOST'] = config.HOST
# mysql.init_app(app)

# Connect to db
# conn = mysql.connect()
# cursor = conn.cursor()

# Execute
# cursor.execute("SELECT * from User")
# data = cursor.fetchone()

# Database Connection
connection = sqlite.connect("store.db")
curser = connection.cursor()

# Creating Table
createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text,password text)"
curser.execute(createTable)

# Inserting user data to the table
user = (1, 'alex', 'pass1')
insertQuery = "INSERT INTO users VALUES(NULL,?,?)"
# curser.execute(insertQuery, user)

# Inserting many users to the database
users = [
    ('Hassan', 'pass'),
    ('ali', 'alus'),
    ('Jonas', 'abdus')
]
curser.executemany(insertQuery, users)

# Selecting from the database
sQuery = "SELECT * FROM users"
for row in curser.execute(sQuery):
    print(row)

connection.commit()
connection.close()
