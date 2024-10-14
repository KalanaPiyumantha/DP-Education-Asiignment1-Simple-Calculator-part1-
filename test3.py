
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "None"
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def select_op(choice):
    if choice in ['+', '-', '*', '/', '^', '%']:
        try:
            a = input("Enter first number: ")
            print(a)
            if a == '#':
                return -1
            a = float(a)
            
        
            b = input("Enter second number: ")
            print(b)
            if b == '#':
                return -1
            b = float(b)
            
            
            
            if choice == '+':
                print(f"{a} + {b} = {add(a, b)}")
            elif choice == '-':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif choice == '*':
                print(f"{a} * {b} = {multiply(a, b)}")
            elif choice == '/':
                result = divide(a, b)
                if b == 0:
                    print ("float division by zero")
                print(f"{a} / {b} = {result}")
            elif choice == '^':
                print(f"{a} ^ {b} = {power(a, b)}")
            elif choice == '%':
                print(f"{a} % {b} = {remainder(a, b)}")

        except ValueError:
            return 0  # Reset

    elif choice == '#':
        return -1  # Terminate
    elif choice == '$':
        print("Resetting...")
        return 0  # Reset
    else:
        print("Unrecognized operation")
        return 0  # Reset

    return 1  # Continue

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    
    if select_op(choice) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
