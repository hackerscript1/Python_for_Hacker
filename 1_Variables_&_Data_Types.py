name = "Bikram"
print(name)
print(len(name))

name_length = 6
print(name_length)

name, name_length = "Bikram", name_length

print(type(name))
print(type(name_length))

name_length = "4"
print(name_length)

name_length = int(name_length)
print(type(name_length))

name_list = ["Bikram", "Susmita", "Karan"]
print(name_list)
print(type(name_list))

name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)

name_tuple = ("Bikram", "Susmita", "Karan")
print(name_tuple)
print(type(name_tuple))

name_dictionary = {
    "name": "Bikram",
    "age": 22,
    "city": "Delhi"
}
print(name_dictionary)
print(type(name_dictionary))

name_boolean = True
print(name_boolean)
print(type(name_boolean))

name_range = range(6)
print(name_range)
print(type(name_range))

name_byte = b"@hackersript1"
print(name_byte)
print(type(name_byte))


