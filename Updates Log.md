# Updates Log

Welcome to the Updates Log!

**Note**: All code files have been created and coded in Visual Studio Code.

## Update 1 - 10/18/2024
### Added Calculator Projects V_1.0 and V_2.0

- **V_1.0**: Simple, Basic Calculator
  - **Features**:
    - Addition
    - Subtraction
    - Multiplication
    - Division

  ```python
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
      print(number1 + number2)

  elif operation == "s":
      print(number1 - number2)

  elif operation == "d":
      print(number1 / number2)

# V_2.0: Added Advanced Calculator Engine #

Features:
All features from V_1.0 (Basic Calculator)
Squaring a number
Cubing a number
Raising a number to a custom power
Calculating square root
Calculating cube root
Calculating nth root

  ```python
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
          print(number1 + number2)
  
      elif operation == "s":
          print(number1 - number2)
  
      elif operation == "d":
          print(number1 / number2)
  
  
  ### Advanced Calculator Engine ###
  
  def advcalculator():
      ### Configuration of operation and numbers ###
      print("Advanced calculator gives the opportunity to use various operations\n")
      
      print("Operations squaring and cubing have been added\n")
  
      print('''If you decide to square, cube, or use a custom exponent, 
            type 0 for number 1; type 'square' or 'cube' 
            into the number 2 input\n''')
      
      advoperation = input("Operation > ").lower()
      advnumber1 = int(input("Number 1 (type (0) if cubing, squaring, or custom exponent usage) > "))
      advnumber2 = int(input("Number 2 > "))
  
      print("Equation Solved:\n")
      ### Equation Solve Engine Code
  
      if advoperation == "m":
          print(advnumber1 * advnumber2)
  
      elif advoperation == "a":
          print(advnumber1 + advnumber2)
  
      elif advoperation == "s":
          print(advnumber1 - advnumber2)
  
      elif advoperation == "d":
          print(advnumber1 / advnumber2)
  
      elif advoperation == "square":
          print(advnumber2 * advnumber2)
      
      elif advoperation == "cubing" or advoperation == "cube":
          print(advnumber2 * advnumber2 * advnumber2)
          
  
  ### Calculator Choose ###
  
  print("Welcome to the Basic + Advanced Calculator\n")
  print("Choose which type of calculator you will pick\n")
  
  calculator = input("Choose which type of calculator (1 for basic, 2 for advanced) > ")
  if calculator == "1":
      print()
      basic_calculator()
  elif calculator == "2":
      print()
      advcalculator()


```
# Update 2 - 12/30/2024 #
# Added Calculator Project V_3.0 (Developed from 10/18/2024 to 12/29/2024) #
# V_3.0: Enhanced Advanced Calculator with Additional Features #

Features:
All features from V_2.0 (Advanced Calculator)
Trigonometric functions: sine, cosine, tangent
Logarithmic functions: base-10 logarithm, natural logarithm
Help Center: Provides detailed information on how to use the calculator and includes special math lessons

```python
import math

def help_center():
    print("""
    # Calculator Help Center

    Welcome to the Calculator Help Center! This guide will help you understand the different features of the calculator, how to use them, and provide free math lessons.

    ## Table of Contents
    - Basic Operations
    - Advanced Operations
    - Trigonometric Functions
    - Logarithmic Functions
    - Special Math Lessons

    ## Basic Operations
    The basic calculator supports the following operations:

    1. **Addition (a)**
       - Adds two numbers.
       - **Example**: 5 + 3 = 8

    2. **Subtraction (s)**
       - Subtracts the second number from the first number.
       - **Example**: 5 - 3 = 2

    3. **Multiplication (m)**
       - Multiplies two numbers.
       - **Example**: 5 * 3 = 15

    4. **Division (d)**
       - Divides the first number by the second number.
       - **Example**: 6 / 3 = 2
       - **Note**: Division by zero is not allowed.

    ### How to Use Basic Operations
    1. Choose the basic calculator by typing 1 when prompted.
    2. Enter the operation (a, s, m, d).
    3. Enter the first number.
    4. Enter the second number.
    5. The result will be displayed.

    ## Advanced Operations
    The advanced calculator supports additional operations:

    1. **Square**
       - Squares a number.
       - **Example**: 4^2 = 16

    2. **Cube**
       - Cubes a number.
       - **Example**: 3^3 = 27

    3. **Power**
       - Raises the first number to the power of the second number.
       - **Example**: 2^3 = 8

    4. **Square Root (sqrt)**
       - Calculates the square root of a number.
       - **Example**: sqrt(16) = 4

    5. **Cube Root (cbrt)**
       - Calculates the cube root of a number.
       - **Example**: cbrt(27) = 3

    6. **Custom Root (root)**
       - Calculates the nth root of a number.
       - **Example**: 8^(1/3) = 2 (cube root)

    ### How to Use Advanced Operations
    1. Choose the advanced calculator by typing 2 when prompted.
    2. Enter the operation (square, cube, power, sqrt, cbrt, root).
    3. Enter the first number (type 0 for square, cube, sqrt, cbrt, or custom root).
    4. Enter the second number.
    5. The result will be displayed.

    ## Trigonometric Functions
    The advanced calculator supports trigonometric functions:

    1. **Sine (sin)**
       - Calculates the sine of an angle (in degrees).
       - **Example**: sin(30) = 0.5

    2. **Cosine (cos)**
       - Calculates the cosine of an angle (in degrees).
       - **Example**: cos(60) = 0.5

    3. **Tangent (tan)**
       - Calculates the tangent of an angle (in degrees).
       - **Example**: tan(45) = 1

    ### How to Use Trigonometric Functions
    1. Choose the advanced calculator by typing 2 when prompted.
    2. Enter the operation (sin, cos, tan).
    3. Enter the first number (type 0 for trigonometric functions).
    4. Enter the angle in degrees.
    5. The result will be displayed.

    ## Logarithmic Functions
    The advanced calculator supports logarithmic functions:

    1. **Logarithm (log)**
       - Calculates the base-10 logarithm of a number.
       - **Example**: log(100) = 2

    2. **Natural Logarithm (ln)**
       - Calculates the natural logarithm of a number.
       - **Example**: ln(2.718) ≈ 1

    ### How to Use Logarithmic Functions
    1. Choose the advanced calculator by typing 2 when prompted.
    2. Enter the operation (log, ln).
    3. Enter the first number (type 0 for logarithmic functions).
    4. Enter the number.
    5. The result will be displayed.

    ## Special Math Lessons
    ### Basic Arithmetic
    - **Addition**: Combining two or more quantities.
    - **Subtraction**: Finding the difference between two quantities.
    - **Multiplication**: Repeated addition of the same number.
    - **Division**: Splitting a number into equal parts.

    ### Exponents and Roots
    - **Exponentiation**: Raising a number to a power.
    - **Square Root**: Finding a number that, when multiplied by itself, gives the original number.
    - **Cube Root**: Finding a number that, when cubed, gives the original number.

    ### Trigonometry
    - **Sine, Cosine, Tangent**: Functions that relate the angles of a triangle to the lengths of its sides.

    ### Logarithms
    - **Logarithm**: The exponent by which a base number must be raised to produce a given number.
    - **Natural Logarithm**: Logarithm with base e (Euler's number).

    For more detailed lessons and examples, visit Khan Academy (https://www.khanacademy.org) or Math is Fun (https://www.mathsisfun.com).
    """)

def basic_calculator():
    operation = input("Operation (a for add, s for subtract, m for multiply, d for divide) > ").lower()
    number1 = float(input("Number 1 > "))
    number2 = float(input("Number 2 > "))

    if operation == "m":
        print(f"Result: {number1 * number2}")
    elif operation == "a":
        print(f"Result: {number1 + number2}")
    elif operation == "s":
        print(f"Result: {number1 - number2}")
    elif operation == "d":
        if number2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"Result: {number1 / number2}")

def advcalculator():
    print("Advanced calculator gives the opportunity to use various operations\n")
    print("Operations: square, cube, power, square root, cube root, custom root, sin, cos, tan, log, ln\n")
    
    advoperation = input("Operation (m for multiply, a for add, s for subtract, d for divide, square, cube, power, sqrt, cbrt, root, sin, cos, tan, log, ln) > ").lower()
    advnumber1 = float(input("Number 1 (type (0) for square, cube, sqrt, cbrt, or custom root) > "))
    advnumber2 = float(input("Number 2 > "))

    print("Equation Solved:\n")
    if advoperation == "m":
        print(f"Result: {advnumber1 * advnumber2}")
    elif advoperation == "a":
        print(f"Result: {advnumber1 + advnumber2}")
    elif advoperation == "s":
        print(f"Result: {advnumber1 - advnumber2}")
    elif advoperation == "d":
        if advnumber2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"Result: {advnumber1 / advnumber2}")
    elif advoperation == "square":
        print(f"Result: {advnumber2 ** 2}")
    elif advoperation == "cube":
        print(f"Result: {advnumber2 ** 3}")
    elif advoperation == "power":
        print(f"Result: {advnumber1 ** advnumber2}")
    elif advoperation == "sqrt":
        if advnumber2 < 0:
            print("Error! Cannot take the square root of a negative number.")
        else:
            print(f"Result: {math.sqrt(advnumber2)}")
    elif advoperation == "cbrt":
        print(f"Result: {advnumber2 ** (1/3)}")
    elif advoperation == "root":
        if advnumber2 == 0:
            print("Error! Cannot take the zeroth root.")
        else:
            print(f"Result: {advnumber1 ** (1/advnumber2)}")
    elif advoperation == "sin":
        print(f"Result: {math.sin(math.radians(advnumber2))}")
    elif advoperation == "cos":
        print(f"Result: {math.cos(math.radians(advnumber2))}")
    elif advoperation == "tan":
        print(f"Result: {math.tan(math.radians(advnumber2))}")
    elif advoperation == "log":
        if advnumber2 <= 0:
            print("Error! Logarithm of a non-positive number is undefined.")
        else:
            print(f"Result: {math.log10(advnumber2)}")
    elif advoperation == "ln":
        if advnumber2 <= 0:
            print("Error! Natural logarithm of a non-positive number is undefined.")
        else:
            print(f"Result: {math.log(advnumber2)}")

print("Welcome to the Basic + Advanced Calculator\n")
print("Choose which type of calculator you will pick\n")

calculator = input("Choose which type of calculator (1 for basic, 2 for advanced, 3 for help center) > ")
if calculator == "1":
    print()
    basic_calculator()
elif calculator == "2":
    print()
    advcalculator()
elif calculator == "3":
    print()
    help_center()

```
Stay tuned for more updates!
This updates log provides a comprehensive and detailed overview of all three versions of the calculator, including features and code examples for each version.
