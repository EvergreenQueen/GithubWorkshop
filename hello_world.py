

def main():
    printstring = ""
    printstring = addition("Hello ", "World!")

    HelloWorld(printstring)


def HelloWorld(printString):
    print(printString)

def addition(x, y):
    return str(x) + str(y)

main()