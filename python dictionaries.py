capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "Vatikan city": "Vatikan city",
            "Italy": "Rome"}

'''print(dir(capitals))
print(help(capitals))
print(capitals.get("India"))

if capitals.get("India"):
    print("That capatal is exists")
else:
    print("Not exists")
capitals.update({"france": "Paris"})
print(capitals)
capitals.pop("India")
capitals.popitem()
capitals.clear()
keys = capitals.keys()
for key in capitals.keys():
    print(key)
values = capitals.values()
for value in capitals.values():
    print(value)'''
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
