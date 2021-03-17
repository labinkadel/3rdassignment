# import jsn package to deal with json in python
import json

print(dir(json))
my_info = {"name": "labin kadel", "age": 27}

with open("my_info.json", "w") as write:
    json.dump(my_info, write)

with open("my_info.json", "r") as read:
    res = json.load(read)
print(res)
