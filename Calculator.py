# Function to add
def addition(a, b):
    return a + b

# Function to subtract
def soustraction(a, b):
    return a - b

# Function to multiply
def multiplication(a, b):
    return a * b

# Function to divide
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division by zero"

# Main function for the calculator
def calculatrice():
    print("Choose the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number of the operation (1/2/3/4): ")

    # Ask for the numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    # Perform the chosen operation
    if operation == '1':
        print("Result:", addition(a, b))
    elif operation == '2':
        print("Result:", soustraction(a, b))
    elif operation == '3':
        print("Result:", multiplication(a, b))
    elif operation == '4':
        print("Result:", division(a, b))
    else:
        print("Invalid operation.")

# Start the calculator
calculatrice()
