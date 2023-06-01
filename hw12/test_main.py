import json

# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
some_data = {'key': 'value'}
file_name = 'test.json'

with open(file_name, "r") as fh:
    unpacked = json.load(fh)
    some_data.update(unpacked)

with open(file_name, "w") as fh:
    json.dump(some_data, fh)
