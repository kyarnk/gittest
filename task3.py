def calc():
    while True:
        num1 = input("Ввод первого числа:")
        num1 = float(num1)

        operator = input("Введите оператор: (+, -, *, /):")
        
        num2 = input("Ввод второго числа:")
        num2 = float(num2)


        if operator == '+':
            result = num1 + num2
            print(f"{num1}+{num2} = {result}")
        elif operator ==  '-':
            result = num1 - num2
            print(f"{num1}-{num2} = {result}")
        elif operator ==  '*':
            result = num1 * num2
            print(f"{num1}*{num2} = {result}")
        elif operator ==  '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1}/{num2} = {result}")
            else:
                print("error delim na 0")
        else:
            print("unknown operator")
calc()
        

    
