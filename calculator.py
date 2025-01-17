import os

# Every def is a function that performs a specific task
class Operation:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def history(self, operation, num1, num2, result):
        symbol = self.get_operation_symbol(operation)
        index = 1  # Par défaut, si le fichier est vide
        if os.path.exists("history.txt"):
            with open("history.txt", "r") as file:
                lines = file.readlines()
                index = len(lines) + 1  # Le prochain index est le nombre de lignes + 1
        with open("history.txt", "a") as file:
            file.write(f"{index}. {num1} {symbol} {num2} = {result}\n")

            
    def delete_selected_history() :
        index_to_delete = int(input("Enter the index of the history entry to delete: "))
        if os.path.exists("history.txt"):
            with open("history.txt", "r") as file:
                lines = file.readlines()
            with open("history.txt", "w") as file:
                for line in lines:
                    if not line.startswith(f"{index_to_delete}."):
                        file.write(line)
    def delete_history() :
        with open("history.txt", "w") as file:
            pass
    def delete_1line_history() :
        with open("history.txt", "r") as file:
            lines = file.readlines()
            lines.pop()
        with open("history.txt", "w") as file:
            for line in lines:
                file.write(line)

    def get_operation_symbol(self, choice):  # This function will return the symbol of the operation
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

    def show_last_10_operations():  # This function displays the last 10 operations from the history file
        if os.path.exists("history.txt"):
            with open("history.txt", "r") as file:
                lines = file.readlines()
                print("\nHistory:")
                for line in lines:
                    print(line.strip())
        else:
            print("No history found.")
    
    def menu_history():
        while True:
            try:
                choice = input("Choose 1 for print history, 2 for delete everything, 3 for delete last line, 4 for delete selected line : ")
                if choice =="1" :
                    Operation.show_last_10_operations()
                if choice =="2" :
                    Operation.delete_history()
                if choice =="3" :
                    Operation.delete_1line_history()
                if choice =="4" :
                    Operation.delete_selected_history()
            except KeyboardInterrupt :
                os.system("cls")
                print("Return to operation menu...")
                break

def exit_program():
    print("Exiting the program.")
    exit()

def main():  # This is the main function that will be executed when the program is run
    operation = Operation()
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. History")
        print("6. Exit")

        choice = input("Enter choice(1/2/3/4/5/6): ")

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
                operation.history (choice, num1, num2, result)  # This will write the history of the operation to a file
            except ValueError:
                print("Can't convert string to number ")
            except ZeroDivisionError:
                print("Can't divide by zero")
        elif choice == '5':
                    os.system("cls")
                    Operation.menu_history()
        elif choice == '6':
            exit_program()
        else:
            print("Invalid input")

# This will run the main function when the program is run.
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:  # This will catch the Ctrl+C signal
            print("\nOperation cancelled by user.")
            break
