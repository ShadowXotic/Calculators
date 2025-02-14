### Introduction Section of Python Basic Calculator ###
### New versions coming out later ###
### Calculator V 2.0 ###

### Choose Operation and Configure 2 numbers for solve ###

### Basic Calculator Engine ###

def basic_calculator():
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


### Advanced Calculator Engine ###

def advcalculator():
    ### Configuration of operation and numbers ###
    print("Advanced calculator gives the opporunity to use various operations\n")
    
    print("Operations squaring and cubing have been added\n")

    print('''If you decide to square, cube, or use a custom exponent, 
          type 0 for number 1; type 'square' or 'cube' 
          into the number 2 input\n''')
    
    advoperation = input("Operation > ").lower()
    advnumber1 = int(input("Number 1 (type (0) if cubing, squaring, or custom exponent usage)> "))
    advnumber2 = int(input("Number 2 > "))

    print("Equation Solved:\n")
    ### Equation Solve Engine Code

    if advoperation == "m":
        print(advnumber1 * advnumber2)

    elif advoperation == "a":
        print(advnumber1+advnumber2)

    elif advoperation == "s":
        print(advnumber1-advnumber2)

    elif advoperation == "d":
        print(advnumber1/advnumber2)

    elif advoperation == "square":
        print(advnumber2*advnumber2)
    
    elif advoperation == "cubing" or advoperation == "cube":
        print(advnumber2*advnumber2*advnumber2)
        

### Calculator Choose ###


print("Welcome to the Basic + Advanced Calculator\n")
print("Choose which type of calculator you will pick\n")
print()

calculator = input("Choose which type of calculator (1) for basic (2) for advanced > ")
if calculator == "1":
    print()
    print()
    basic_calculator()

elif calculator == "2":
    print()
    print()
    advcalculator()