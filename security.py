from user import User
SECRET_KEY = 'Un3v3rkn0w@asd'

# users = {
#     User(1, 'alex', 'thepass')
# }

# userNameMapping = {x.username: x for x in users}
# userIdMapping = {x.id: x for x in users}


# Authenticate User
def authenticate(username, password):
    # user = userNameMapping.get(username, None)
    user = User.findUserByUsername(username)
    if user and user.password == password:
        return user


# identity
def identity(payload):
    userId = payload['identity']
    # return userIdMapping.get(userId, None)
    return User.findUserById(userId)
