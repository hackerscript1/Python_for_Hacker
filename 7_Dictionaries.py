dict1 = {
    "name" : "Bikram",
    "Subjects" : ["C", "Java", "Python"],
    "CGPA" : 84.6,
    "Address" : {
        "Street" : "123 Main St",
        "City" : "New York",
        "State" : "NY"
    }
}

print(dict1)
print(type(dict))
print(len(dict1))

print(dict1["name"])
print(dict1.get("name"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1["name"] = 1
print(dict1)

dict1["Address"] = "India"
print(dict1)

dict1["name"] = 0
print(dict1)

dict1.update({"name" : "Bikram"})
print(dict1)

dict1.pop("Address")
print(dict1)

del dict1["CGPA"]
print(dict1)

dict1["Address"] = {"Street" : "123 Main St", "City" : "New York", "State" : "NY"}
print(dict1)

dicr2 = {}
print(dicr2)

dict3 = dict()
print(dict3)


