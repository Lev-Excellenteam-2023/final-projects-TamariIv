import json


def to_json(filename, *args):
    with open(filename + ".json", "w") as file:
        json.dump(args, file, indent=4)
