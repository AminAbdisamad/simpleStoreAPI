import sqlite3 as sqllite
from flask_restful import Resource, reqparse
# from conn import Database


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findUserByUsername(cls, username):
        connection = sqllite.connect("store.db")
        curser = connection.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        result = curser.execute(query, (username,))
        row = result.fetchone()
        if row:
            # user = User(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def findUserById(cls, _id):
        connection = sqllite.connect("store.db")
        curser = connection.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        result = curser.execute(query, (_id,))
        row = result.fetchone()
        if row:
            # user = User(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user


class RegisterUser(Resource):
    # Requesting username data
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This can not be blank'
                        )
    # Requesting password data
    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This can not be blank'
                        )

    def post(self):

        # Getting username and password from the client
        data = RegisterUser.parser.parse_args()
        # Database connection
        connection = sqllite.connect('store.db')
        curser = connection.cursor()

        # Inserting users to database
        query = "INSERT INTO users VALUES (NULL,?,?)"

        curser.execute(
            query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {"message": "User created successfully"}, 201
