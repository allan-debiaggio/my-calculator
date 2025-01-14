def calculator() :
    print ("Hello ! Welcome to the calculator ! :D")

def number_type():
    while True :
        try :
            user_choice = input("Type 1 to use integers, 2 to use floats : ")
            if user_choice == "1" :
                number1= int(input("Give the first number you want to use : "))
                number2= int(input("Give the second number you want to use : "))
            elif user_choice == "2" :
                number1= float(input("Give the first number you want to use : "))
                number2 = float(input("Give the second number you want to use : "))
            else :
                print("I did not understand your request.")
                continue
        except KeyboardInterrupt : 
            print("Exiting calculator...")
            break
        return number1,number2

def operator(a,b):
    while True :
        try : 
            user_choice = input("Type the operator you want to use : \n+(add), -(minus),*(multiply),/(divide) : ")
            if user_choice == "+" :
                return a + b
            elif user_choice == "-" :
                return a - b
            elif user_choice == "*" :
                return a * b
            elif user_choice == "/" :
                return a / b
            else : 
                print("I did not understand your request.")
                continue
        except KeyboardInterrupt :
            print("Exiting calculator...")
            break
    

calculator()
number1, number2 = number_type()
print(operator(number1,number2))