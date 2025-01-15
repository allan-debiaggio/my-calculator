import os
#Every def is a function that performs a specific task
class Operation:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

    def history(self, operation, num1, num2, result): # This function will write the history of the operations to a file
        symbol = self.get_operation_symbol(operation)
        with open("history.txt", "a") as file:
            file.write(f"{num1} {symbol} {num2} = {result}\n")

    def get_operation_symbol(self, choice): # This function will return the symbol of the operation
        if choice == '1':
            return '+'
        elif choice == '2':
            return '-'
        elif choice == '3':
            return '*'
        elif choice == '4':
            return '/'
        else:
            return ''

def main(): # This is the main function that will be executed when the program is run
    operation = Operation()
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
                    result = operation.add(num1, num2)
                elif choice == '2':
                    result = operation.subtract(num1, num2)
                elif choice == '3':
                    result = operation.multiply(num1, num2)
                elif choice == '4':
                    result = operation.divide(num1, num2)

                symbol = operation.get_operation_symbol(choice)
                print(f"{num1} {symbol} {num2} = {result}")
                operation.history(choice, num1, num2, result) # This will write the history of the operation to a file
            except ValueError as e:
                print(e)
        else:
            print("Invalid input")
        

# This will run the main function when the program is run
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt: # This will catch the Ctrl+C signal
            print("\nOperation cancelled by user.")
            break
