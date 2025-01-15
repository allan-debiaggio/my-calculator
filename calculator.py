import os
#Every def is a function that performs a specific task
def add(x, y):
    return x + y

def subtract(x, y):
     return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
#This is the main function that will be called when the program is run
def main():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                os.system("cls")
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                os.system("cls")
                print(e)
                print("Please try again.")
        else:
            print("Invalid input")
#This function will write the history of the operations to a file
def history(operation, num1, num2, result):
    with open("history.txt", "a") as file:
        file.write(f"{operation}: {num1} and {num2} = {result}\n")


if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt: # This will catch the Ctrl+C signal
            print("\nOperation cancelled by user.")
            break
