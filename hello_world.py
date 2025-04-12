

def main():
    HelloWorld(addition("Hello", " World!"))
    HelloWorld(addition(1, 2))

def HelloWorld(printString):
    print(printString)

def addition(a, b):
    return str(a) + str(b)


def test_case_1():
    main()

def test_case_2():
    main()
    main()
    HelloWorld(addition("Game", "spawn"))


test_case_1()
test_case_2()