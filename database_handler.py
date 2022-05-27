import json


def getDatabase():
    with open('database.json', "r") as read_file:
        data = json.load(read_file)
    return data
