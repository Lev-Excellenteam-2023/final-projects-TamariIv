import json


def to_json(filename, *args):
    with open(filename + ".json", "w") as file:
        for arg in args:
            json.dump(arg, file)
