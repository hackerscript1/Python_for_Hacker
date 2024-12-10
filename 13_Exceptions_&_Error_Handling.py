print(1)
    #print(2)  #given an error

try:
    f = open("asdas")
except:
    print("The file does not exist")

# try:
#     sadssdsf
# except:
#     print("The file does not exist")

try:
    f = open("asdas")
except Exception as e:
    print(e)

# try:
#     asdasad
# except Exception as e:
#     print(e)

try:
    f = open("asdas")
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print(e)

# try:
#     sasd; sdada; asdas
# except FileNotFoundError:
#     print("The file does not exist")
# except Exception as e:
#     print(e)

try:
    f = open("top-100.txt")
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print(e)
finally:
    print("this message!")

n = 100
if n == 0:
    raise Exception("n can't be 0")

print(1/n)

# n = 0
# if n == 0:
#     raise Exception("n can't be 0")

# print(1/n)

# n = 'asda'
# if n == 0:
#     raise Exception("n can't be 0")

# print(1/n)

# n = 'asda'
# if n == 0:
#     raise Exception("n can't be 0")
# if type(n) is not int:
#     raise Exception("n must be an integer")

# print(1/n)

n = 100
if n == 0:
    raise Exception("n can't be 0")
if type(n) is not int:
    raise Exception("n must be an integer")

print(1/n)

n = 1
assert(n != 0)
print(1/n)

n = 0
assert(n != 0)
print(1/n)

