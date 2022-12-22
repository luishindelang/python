import json


def readData(path):
    with open('./db/'+path, 'r', encoding='utf-8') as file:
        return json.load(file)


def writeData(path, data):
    with open('./db/'+path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
