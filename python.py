"""
Tmam let's begin this code is made to help you if you wanna remember python syntax.
I hope It helps anyone who needs it.
ok let's begin, btw this thing is a multi line comment which allows me to right
multi line text which will be ignored be the user

"""
# To make a comment you use '#' and for multi line comments u put your txt between """"   """

# printing text in a compiler:
print("printed text in the compiler\n")

# data types:
Integer = 10
Double = 10.10
String = "Hello"
Characters = 'z'
List = ["here", "I can ", "Enter bunch of elements", 4, "In python you can enter different data types in a list"]

# getting input from the user
User_Entry = input("Enter you name:\n")
print(User_Entry, "that is his name")

# for loops (I am going to iterate in the for loop using range function)
# You can iterate in the loop by other methods but I like this method
for i in range(10):
    print(i, "\n")

# While loops
# In while loops you need to acheive a condition to keep working
x = 0
print("See (btw the loop will stop at x = 2)")
while x < 2:

    print(x)
    x = x+1

print(x, "\n")

# Functions:
# in the function you can write a block of code which won't be executed until you
# call it (the use of the function is that you can call it any time you wanted


def funcc():
    print("This text will be executed in the end cause I don't intend to call the function until then")

# If statements and try catch:
# In here I am gonna make a simple calculator using if statements
# And while loops and try catch to catch errors
y = True
while y:
    try:
        d = int(input("Enter the first number"))
        d2 = int(input("Enter the second number"))
        operation = input("Enter the operation you wanna do ")
    except:
        print("Invalid try again")
        continue
    if operation == "/":
        print(d/d2)
    elif operation == "+":
        print(d+d2)
    elif operation == "-":
        print(d-d2)
    elif operation == "^":
        print(pow(d,d2))
    elif operation == "%":
        print(d%d2)
    elif operation == "//":
        print(d//d2)
    elif operation == "*":
        print(d*d2)
    else:
        print("You entered invalid operation try once more without fucking things up")
        continue
    y = False

