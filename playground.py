#TODO 1: Create a function called add where you can pass in x number of arguments and sum them

# 1st: Create the function to take on unlimited number of arguments
def add(*args): #asterics will always group arguments into a tuple
    print(args[0])

    total = 0
    for num in args:
        total += num
    print(total)
add(1,2,4,6, 7)
