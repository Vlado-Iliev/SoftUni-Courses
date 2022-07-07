from json import loads, dumps

users_db_path_file = './users.txt'


def register(username, password):
    with open(users_db_path_file, 'r') as users_db:
        for line in users_db:
            users = loads(line.strip())
            if users['username'] == username:
                return False

    with open(users_db_path_file, 'a') as users_db:
        user = {
            'username': username,
            'password': password
        }

        user_json = dumps(user)
        users_db.write(user_json + '\n')

    return True


def login(username, password):
    with open(users_db_path_file, 'r') as users_db:
        for line in users_db:
            users = loads(line.strip())
            if users['username'] == username and users['password'] == password:
                return True

            return False
