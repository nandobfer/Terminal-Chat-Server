import json


def getDatabase():
    with open('database.json', "r") as read_file:
        data = json.load(read_file)
    return data


def signUp(user):
    data = getDatabase()
    data.update(user)

    with open('database.json', "w") as file:
        file.write(data)
        return True
