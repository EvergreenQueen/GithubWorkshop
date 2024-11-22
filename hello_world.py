

def main():
    HelloWorld(addition("Hello", " World!"))
    HelloWorld(addition(1, 2))

def HelloWorld(printString):
    print(printString)

def addition(a, b):
    return str(a) + str(b)


def test_case_1():
    main()


test_case_1()