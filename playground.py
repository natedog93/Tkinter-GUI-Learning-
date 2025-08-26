# How come arguments are not being listed in properties, but can be used by typping them in
#Advanced Arguments
 #Keyword Arguments
    #Solve by creating arugments that have default values - Chagne function declaration
    # def my_function(a=1, b=2, c=3):
        #do this with a
        #then do this with b
    #my_function() - does not require keyword arguments if you are going to change declaration above "Prime" the function
    # What if I want to modify b?
        #my_function(b = 5)

#TODO 1: Create a function called add where you can pass in x number of arguments and sum them

# 1st: Create the function to take on unlimited number of arguments
def add(*args): #asterics will always group arguments into a tuple
    print(args[0])

    total = 0
    for num in args:
        total += num
    print(total)
add(1,2,4,6, 7)

def calculate(**kwargs): #Turns data type into a dictionary
    print(kwargs)
    # for key, value in kwargs.items(): #allows you to loop through dictionary using .items to print key/value
    #     print(key)
    #     print(value)

    print(kwargs["add"]) #could also index the key to print out the value 3 or other

calculate(add= 3, multiply = 5)

#could also do the below for the above - allows for more flexibility in working with arguments and name values passing
# into function:
def calculate2(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate2(2, add = 3, multiply = 5)

class Car:

    def __init__(self, **kw): #**kw are all optional arguments that you can pass in when initializing the class
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("color")
        self.seats = kw.get("seats")

#going to get an error when calling the below if you use brackets for self.make or self.model
#Change the brackets to parenthasis add .get method. This will search through your kw dictionary and pass if no key is found
my_car = Car(model = "GT-R") # won't see any of the properties, just like tkinter - refering to optional keyword arguments

print(my_car.model)