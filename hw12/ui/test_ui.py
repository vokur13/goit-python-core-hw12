import json

file_name = '../test.json'

with open(file_name, "r") as fh:
    unpacked = json.load(fh)

print(unpacked)
