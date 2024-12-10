string1 = 'I am a string!'
string2 = "I am a string too!"
print(string1)
print(string2)

string3 = '''I am a long
long 
string'''
print(string3)

string4 = "I\"m a string"
print(string4)

string5 = 'I"m a string'
print(string5)

string6 = "I\"m a string\nI\"m a new line"
string6 = "\\ \x41\x42\x43\x44\x45"
print(string6)

string7 = "aaaaaaaaaa"
print(string7)
print(len(string7))

string7 = "a" * 10
print(string7)
print(len(string7))

print("Bikram" in string4)
print(string4.startswith("I"))

print(string4.index("string"))
print(string4.upper())
print(string4.lower())

messy_string = "     Messy String!     "
print(messy_string)
print(messy_string.strip())

print(messy_string.replace("!", "?").strip())
print(messy_string.replace("String", "Example"))

string4 = "I am a string!"
print(string4)
print(string4.encode())
print(string4.encode("utf-8"))

print(string4.rjust(25))
print(string4.rjust(25, 'X'))

print(string4.ljust(25))
print(string4.ljust(25, 'X'))

print("I am " + "a string!")
print("String 4 is " + str(len(string4)) + " characters")

print(1 + 1)
print("1" + "1")
print(type("1" + "1"))

print("String 4 is {} characters".format(len(string4)))
print("{} {} {}".format(len(string4), 5.0, 0x12))
print("{0} {2} {1}".format(len(string4), 5.0, 0x12))
print("{length}".format(length = len(string4)))

length = len(string4)
print(f"String 4 is {length} characters")
print("String 4 is {length} characters".format(length = len(string4)))

print("String 4 is {length:.1f} characters".format(length = len(string4)))
print("String 4 is {length:.2f} characters".format(length = len(string4)))
print("String 4 is {length:.3f} characters".format(length = len(string4)))
print("String 4 is {length:.4f} characters".format(length = len(string4)))

print("String 4 is {length:x} characters".format(length = len(string4))) #hex
print("String 4 is {length:b} characters".format(length = len(string4))) #binary
print("String 4 is {length:o} characters".format(length = len(string4))) #octal

print("String 4 is %d characters" % len(string4))
print("String 4 is %f characters" % len(string4))
print("String 4 is %x characters" % len(string4))

