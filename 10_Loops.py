a = 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)

a = 1
while a <= 5:
    print(a)
    a += 1

for i in [0, 1, 2, 3, 4, 5]:
    print(i + 6)

for i in range(6):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 6, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in range(3):
    for j in range(3):
        print(i, j)

for i in range(5):
    if i == 2:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass
    print(i)

for c in "string":
    print(c)

for key, value in {"a":1, "b":2, "c":3, "d":4}.items():
    print(key, value)


