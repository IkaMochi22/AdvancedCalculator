import math
import cmath

# Operator functions
def Addition(x, y):
    return (x + y)

def Subtraction(x, y):
    return (x - y)

def Multiplication(x, y):
    return (x * y)

def Division(x, y):
    try:
        return (x / y)
    
    except ZeroDivisionError:
        return "Undefined"

def SquareRoot(x):
    return (cmath.sqrt(x))

def print_factors(x):
    print("The factors of",x, "are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print((i), '\t\t', format(str(reversed((i)))))

def Exponents(x, y):
    return (x **y)

def QuadraticFormula(x,y,z):
    return ((-y + cmath.sqrt(y**2 - 4*x*z))/(2*x)) , ((-y - cmath.sqrt(y**2 - 4*x*z))/(2*x))

# Asks user for desired operation
print("Select operation.")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. Square Root")
print(" 6. Factors")
print(" 7. Exponents")
print(" 8. Quadratic Formula")

# Variables
num = 0
num1 = 0
num2 = 0
num3 = 0

a = 0
b = 0
c = 0

# Maths
while True: 
    # Take user input
    choice = input("Enter choice (1, 2, 3, 4, 5, 6, 7, or 8): ")

    # checks if choice is one of the six options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try: 
          num1 = int(input("Enter number: "))
          if choice in ('1', '2', '3', '4', '7'):
              num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", Addition(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", Multiplication(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", Division(num1, num2))
        elif choice == '5':
            print(cmath.sqrt(num1))
        elif choice == '6':
            print_factors(num1)
        else:
            print(num1,"^", num2, "=", Exponents(num1, num2))
    if choice == '8':
        try:
            num1 = int(input("Enter your a value: "))
            num2 = int(input("Enter your b value: "))
            num3 = int(input("Enter your c value: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        print("-", num2, "+-", "√(", num2, "^2 - 4(", num1, ")(", num3, "))")
        print("--------------------------------------")
        print('\t' "2(", num1, ")")
        print(QuadraticFormula(num1, num2, num3))
