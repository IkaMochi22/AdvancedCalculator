# This allows the user to choose how many terms to use in the operations
import math
import cmath


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

def Exponents(x, y):
    return (x**y)

def SquareRoot(x):
    return (cmath.sqrt(x))

def factors(x):
    neg = False

    if x < 0:
        neg = True
        x = -x

    factors_list = [1, x]
    complete_list = []

    for i in range(2, math.ceil(math.sqrt(x) + 1)):
        if x % i == 0:
            factors_list += (i, x // i)

    if neg:
        complete_list = factors_list + list(reversed(factors_list))

    else:
        complete_list = factors_list

    return complete_list

def QuadraticFormula(x, y, z):
    return ((-y + cmath.sqrt(y**2 - 4*x*z)) / (2*x)) ,\
    ((-y - cmath.sqrt(y**2 - 4*x*z)) / (2*x))


print("Select operation.")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. Square Root")
print(" 6. Factors")
print(" 7. Exponents")
print(" 8. Quadratic Formula")

num = 0
num1 = 0
num2 = 0
num3 = 0

a = 0
b = 0
c = 0

while True:
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
            print(f"The factors of {num1} are: ")
            res = factors(num1)

            for i in range(0, len(res), 2):
                print(res[i], "\t\t", res[i+1])

        else:
            print(num1, "^", num2, "=", Exponent(num1, num2))

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
