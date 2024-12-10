def function1():
    print("Hello from fuction1!")

function1()
function1()


def function2():
    return "Hello from fuction2!"

return_from_fuction2 = function2()
print(return_from_fuction2)


def function3(s):
    print("\t{}".format(s))

function3("Parameter1")
function3("Parameter2")


def function4(s1, s2):
    print("{} {}".format(s1, s2))

function4("s1", "s2")
function4("Parameter1", "Parameter2")

function4("Any", "Things")
function4(s1="Things", s2="Any")
function4(s2="Any", s1="Things")


def function5(s1="default"):
    print("{}".format(s1))

function5()
function5("Anything!")


def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("Function6!")
function6("Function6!", "a")
function6("Function6!", "a", "b", "c")


def function7(**ks):
    for a in ks:
        print("{}:{}".format(a, ks[a]))

function7(a="A", b="B", c="C")


def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("Hello", 3.14, 5, [1, 2, 3])


v = 100
print(v)

def function9():
    v = 5
    v += 1
    print(v)

function9()

print(v)


v = 100
print(v)

def function9():
    global v  # Use global keyword to modify the global variable
    v += 1
    print(v)

function9()

print(v)


def function10():
    print("Hello from Function10")

def function11():
    print("Hello from Function11")

function10()
function11()


def function10():
    print("Hello from Function10")

def function11():
    function10()
    print("Hello from Function11")

function11()


def function12(x):
    print(x)
    if x > 0:
        function12(x - 1)

function12(5)


def function13(x):
    if x > 0:
        function13(x - 1)
        print(x)

function13(5)


def function14(x):
    while x > 0:
        print(x)
        x -= 1

function14(5)


def function15(x):
    for i in range(x, 0, -1):
        print(i)

function15(5)


