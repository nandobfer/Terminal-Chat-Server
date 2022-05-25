import json


def getDatabase():
    with open('database.json', "r") as read_file:
        data = json.load(read_file)
    return data


def signUp(user, password):
    data = getDatabase()
    data.update({user: password})

    with open('database.json', "w") as file:
        file.write(data)
        return True
