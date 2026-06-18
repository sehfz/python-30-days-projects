import math
def show_menu():
    print("\n" + "="*40)
    print("     SCIENTIFIC CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sine (sin x)")
    print("8. Cosine (cos x)")
    print("9. Tangent (tan x)")
    print("10. Logarithm (log x)")
    print("11. Exit")
    print("="*40)

def addition():
    n = int(input("How many numbers do you want to add? "))
    total = 0
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        total += num
    print(f"Sum = {total}")

def subtraction():
    n = int(input("How many numbers do you want to subtract? "))
    if n < 1:
        print("You need at least one number.")
        return
    result = float(input("Enter base number: "))
    for i in range(n - 1):
        num = float(input(f"Enter number to subtract ({i+1}): "))
        result -= num
    print(f"Result = {result}")

def multiplication():
    n= int(input("How many numbers do you want to multiply?"))
    result=1
    for i in range(n):
        num=float(input(f"Enter number {i+1}: "))
        result *= num
    print(f"product={result}")

def division():
    n=int(input("How many numbers do you want to divide?"))
    if n < 2:
        print("You need at least two numbers for division.")
        return
    result = float(input("Enter base number: "))
    for i in range(n-1):
        num = float(input(f"Enter divisor ({i+1}): "))
        if num==0:
            print("Error: Division by zero is not allowed!")
            return
        result/=num
    print (f"result = {result}")

while True:
    show_menu()
    choice=input("Choose 1-11 : ")

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        multiplication()
    
    elif choice == "4":
        division()
            
    elif choice == "5":
        x = float(input("Enter base: "))
        y = float(input("Enter exponent: "))
        result = math.pow(x, y)
        print(f"{x} ^ {y} = {result}")
            
    
    elif choice == "6":
        x = float(input("Enter number: "))
        if x < 0:
            print("Error: Cannot calculate square root of negative number!")
        else:
            result = math.sqrt(x)
            print(f"√{x} = {result}")
    
    elif choice == "7":
        x = float(input("Enter angle in degrees: "))
        rad = math.radians(x)
        result = math.sin(rad)
        print(f"sin({x}°) = {result}")
    
    elif choice == "8":
        x = float(input("Enter angle in degrees: "))
        rad = math.radians(x)
        result = math.cos(rad)
        print(f"cos({x}°) = {result}")

    elif choice == "9":
        x = float(input("Enter angle in degrees: "))
        rad = math.radians(x)
        if math.cos(rad) == 0:
            print("Error: Tangent undefined for this angle!")
        else:
            result = math.tan(rad)
            print(f"tan({x}°) = {result}")

    elif choice == "10":    
        x = float(input("Enter number: "))
        if x <= 0:
            print("Error: Logarithm undefined for zero or negative numbers!")
        else:
            result = math.log(x)
            print(f"ln({x}) = {result}")        

    elif choice == "11":    
        print("Goodbye")
        break
    else:
        print(" Invalid choice! Please enter 1-11.")
