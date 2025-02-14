### Introduction Section of Python Basic Calculator ###
### New versions coming out later ###
### Calculator V 1.0 ###

print("Welcome to the Python Basic Calculator\n")
print("If you need the instructions, please go to"
     "the Python basic calculator instructions")

### Choose Operation and Configure 2 numbers for solve ###

operation = input("Operation > ").lower()
number1 = int(input("Number 1 > "))
number2 = int(input("Number 2 > "))

### Equation Solve Engine Code ###

if operation == "m":
    print(number1 * number2)

elif operation == "a":
    print(number1+number2)

elif operation == "s":
    print(number1-number2)

elif operation == "d":
    print(number1/number2)
    