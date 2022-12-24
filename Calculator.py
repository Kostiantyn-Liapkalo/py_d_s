result = 0
is_number = True
operand = None

while True:
    
    user_input = input("Enter data: ")
    
    if user_input != "=":
        if is_number == True:
            try:
                operator = int(user_input)
            except ValueError:
                print(f"{user_input} not numbbr. Enter number")
                continue
            is_number = False
            operand = int(user_input)
        elif is_number == False:
            if user_input not in "+-*/":
                print(f"{user_input} not operand. Enter operand.")
                continue
            is_number = True
            operand = user_input
            continue
        if operand == None or operand == "+":
            result += operand
        elif operand == "-":
            result -= operand
        elif operand == "*":
            result *= operand
        elif operand == "/":
            result //= operand
    else:
        print(result)
        break


