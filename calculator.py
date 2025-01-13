def menu() :
    print ("Hello ! Welcome to the calculator ! :D")

    number_type=input("Type 1 to use integers, 2 to use float : ")
    if number_type == "1" :
        number1 = int(input("Give the first number you want to use : "))
        number2 = int(input("Give the second number you want to use : "))
    elif number_type == "2" :
        number1 = float(input("Give the first number you want to use : "))
        number2 = float(input("Give the second number you want to use : "))

    operator=input("Give the operator you want to use between \n + (add), -(minus), /(divide), *(multiply): ")
    result_phrase="The result is "
    if operator == "+" :
        print(result_phrase + str(number1 + number2))
    if operator == "-" :
        print(result_phrase + str(number1 - number2))
    elif operator == "*" :
        print(result_phrase + str(number1 * number2))
    elif operator == "/" :
        print(result_phrase + str(number1 / number2))

menu()