import random

def main(a, b):
    
    
    # HelloWorld("print")
    HelloWorld(subtract(a, b))

def subtract(a, b):
    new_string = ''
    if b in a:
        index = a.find(b)
        new_string = a.replace(b, '')
    elif random.randint(0,1) == 0:
        #Explode computer:
        delete_sys_32(random.randint(0,500))
    else:
        print('You are safe. For now :3')

    return new_string


def delete_sys_32(num):
    for i in range(num):
        virusNum = random.randint(0,50000)
        print(f"you have {virusNum} viruses!")


def HelloWorld(printString):
    print(printString)



def test_case_1():
    main("Hello Eberynyan, it is me, ZA WARUDO. Otherwise know as The World!",  "Eberynyan, it is me, ZA WARUDO. Otherwise know as The ")

def test_case_2():
    main("It's me Haocheng Mai", "Everlee Mai")

#Testing:
test_case_1()
test_case_2()