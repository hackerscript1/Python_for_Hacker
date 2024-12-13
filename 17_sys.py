import sys
print(sys.version)
print(sys.executable)
print(sys.platform)

for line in sys.stdin:
    if line.strip() == "exit":
        break
    else:
        print(">>> {}".format(line.strip()))
        print("Exploiting...")

for i in range(1, 5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

for i in range(1, 5):
    print(i)


import time

for i in range(0, 51):
    time.sleep(0.1)
    sys.stdout.write("{} [{}{}]\r".format(i, '#' * i, '.' * (50 - i)))
    sys.stdout.flush()
sys.stdout.write("\n")

print(sys.argv)

if len(sys.argv) != 3:
    print("[X] To run {} enter a username and password".format(sys.arg[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

print("Username: {}".format(username))
print("Password: {}".format(password))

print(sys.path)
print(sys.modules)

sys.exit(0)


