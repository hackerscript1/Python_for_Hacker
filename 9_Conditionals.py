if True:
    print("True")

if False:
    print("False")

if not False:
    print("Not False")

if 1 < 1:
    print("1 is less than 1")
elif 1 <= 0:
    print("1 is less than or equal to 0")
else:
    print("1 is not less than 1")

if 1 < 1:
    print("1 is less than 1")
elif 1 <= 1:
    print("1 is less than or equal to 0")
else:
    print("1 is not less than 1")

if 1 < 1:
    print("1 is less than 1")
elif 1 < 1:
    print("1 is less than or equal to 0")
elif 2 <= 2:
    print("2 is less than or equal to 2")
else:
    print("1 is not less than 1")

if 1 > 0 and 0 < 1:
    print("Both conditions are true")

if 1 > 0 or 0 < 1:
    print("At least one condition is true")

if not (1 > 0 and 0 < 1):
    print("Both conditions are false")

if not (1 > 0 or 0 < 1):
    print("At least one condition is false")

if not (1 > 0 and 0 < 1) or not (1 > 0 or 0 < 1):
    print("At least one condition is false")

if not (1 > 0 and 0 < 1) or (1 > 0 or 0 < 1):
    print("Both conditions are true")

if 0 < 1 : print("0 < 1")
print("1 >= 1") if 1 >= 1 else print("1 < 1")

if 1 >= 1:
    print("1 >= 1")
else:
    print("1 < 1")

if 0 > 1:
    print("1")
elif 0 < 1:
    print("2")
else:
    print("3")

print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")

