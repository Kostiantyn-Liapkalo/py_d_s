# rate = 1.68
# value_day = 20
# value_night = 10
# payment = (value_day * rate) + rate * (value_night / 2)
# print(payment)


# first_name = "Stepan"
# last_name = "Bandera"
# full_name = first_name + " " + last_name
# message = f"Dear {first_name} we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"
# print(message)


# length = "2.75"
# width = "1.75"
# area = float(length) * float(width)
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)


# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# area = length * width
# print(area)


# name = input("What is your name? ")
# print(f"Hello {name}")


# age = input("How old are you? ")

# if int(age) >= 18:
#     print("You are adult already.")
# else:
#     print("You are infant yet.")


# a = input('Введіть число')
# a = int(a)
# if a > 0:
#     print('Число позитивне')
# elif a < 0:
#     print("Число негативне")
# else:
#     print('Це число - нуль')


# name = "Taras"
# age = 18
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")


# is_nice = False
# state = "nice" if is_nice else "not nice"

# print(state)


# if x >= 0:
#     if y >= 0:               # x > 0, y > 0
#         print("Перша чверть")
#     else:                    # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:               # x < 0, y > 0
#         print("Друга чверть")
#     else:                    # x < 0, y < 0
#         print("Третя чверть")


# fruit = 'apple'
# for char in fruit:
#     print(char)

# a = 1
# while a <= 5:
#     print(a)
#     a = a + 1


# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a += 1


# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break


# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)


# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number -= 1
#         if number < 0:
#             break


# val = "a"
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")


# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")


# while True:
#     age = input("How old are you?")
#     try:
#         age = int(age)
#         if age >= 18:
#             print("Welcome men")
#             break
#         else:
#             print("You are children!")
#             break
#     except ValueError:
#         print(f'{age} is not number. Pleas access number!')
#     finally:
#         print("-"*50)


# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#      ("ok")
# else:
#     print(None)


# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience >= 1 and work_experience <= 5:
#     developer_type = "Middle"
#     print("Middle")
# elif work_experience == 1:
#     developer_type = "Junior"
#     print("Junior")
# else:
#     developer_type = "Senior"
# print("Senior")


# num = int(input("Enter a number: "))

# if num % 2:
#     if num % :
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# num = int(input("Enter an integer number: "))

# is_even = True if num % 2 == 0 else False


# num = int(input("Введіть ціле число (0 до 10): "))
# count = 10 - num
# i = 1
# while i <= count:
#     print(f"Ітерація {i}")
#     i += 1

# print("Програма закінчена")


# num = int(input("Введите целое: "))
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print("Сумма цифр числа равна: ", sum)


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num >+ 1:
#     sum = sum + num
#     num -= 1


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while sum <= num:
#     if sum < num:
#         sum += 1
#         print(sum)


# num = int(input("Enter the integer (0 to 100): "))
# Sum = 0
# for i in range(0, num):  # peculiarity thats why 101
#     Sum = Sum+i
# print(Sum)


# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for i in message:
#     if i == search:
#         result += 1
# print(result)


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = min(first, second)
# while first != 0 and second != 0:
#     if first >= second:
#         first %= second
#     else:
#         second %= first
#     print(first or second)


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = min(first, second)

# while not first % gcd == 0 or not second % gcd == 0:
#     gcd -= 1


# num = int(input("Введіть число (0 для виходу): "))

# while num != 0:
#     repeat = int(input("Скільки разів помножити число на 2? "))
#     for i in range(repeat):
#         num = num * 2
#     print(num)
#     num = int(input("Введіть число (0 для виходу): "))

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(0, num + 1):
#         if i % 2 != 0:
#             continue

#         sum = sum + i


# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#     if ch == " " or ch == "!":
#         encoded_message += ch
#         continue
#     pos =
#                         ')
#     pos = (pos + offset) % 26
#     new_char = chr(pos + ord("a"))
#     encoded_message = encoded_message + new_char

# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#     mesto = message.find(ch)
#     new_mesto = mesto + offset
#     if ch in message:
#         encoded_message += ch
#     else:
#         encoded_message += ch
# print (encoded_message)


# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""

# for ch in message:

#     char_as_int = ord(ch)

#     if 65 <= char_as_int <= 90 or 97 <= char_as_int <= 122:
#         cod = char_as_int + offset % 26
#         if not (65 <= cod <= 90 or 97 <= cod <= 122):
#             cod -= 26
#         new_char = chr(cod)
#         encoded_message += new_char

#     else:
# encoded_message += ch

# result = None
# wait_for_number = True

# while True:

#     operand_ferst = int(float(input("Enter your operand: ")))
#     operand_second = int(float(input("Enter your operand: ")))
#     operator = input("Enter your operator: ")

#     if operator == "+":
#         result = operand_ferst + operand_second
#         print(result)
#     elif operator == "-":
#         result = operand_ferst - operand_second
#         print(result)
#     elif operator == "*":
#         result = operand_ferst * operand_second
#         print(result)
#     else:
#         print("You do not enter a operator!")
#     try:
#         result = operand_ferst / operand_second
#         print(result)
#     except ZeroDivisionError:
#         print("Zero not Divi



operand = None
operator = None
wait_for_number = True

def funk1_operand():
    while wait_for_number:
        try:
            global operand1
            operand1 = float(input('Write a number: '))
            break
        except:
            print('Please, write a number')

def funk2_operand():
    while wait_for_number:
        try:
            global operand2
            operand2 = float(input('Write a number: '))
            break
        except:
            print('Please, write a number')

def funk_operator():
    global operator
    operator = input('Operator: ')
    while operator not in ('+', '-', '*', '/', '='):
        operator = input('Please, write -, +, *, or /: ')

def funk_result1():
    global result
    if operator == '-':
        result = operand1 - operand2
    elif operator == '+':
        result = operand1 + operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2

def funk_result2():
    global result
    if operator == '-':
        result = result - operand
    elif operator == '+':
        result = result + operand
    elif operator == '*':
        result = result * operand
    elif operator == '/':
        result = result / operand


funk1_operand() #operand1 (first float number)
funk_operator() #operator (-, +, *, /)
funk2_operand() #operand2 (second float number)
funk_result1()  #result   (result operator operand)

while operator != '=':
    funk_operator()  # operator (-, +, *, /)
    if operator == '=':
        break
    while wait_for_number:
        try:
            operand = float(input('Write a number: '))
            break
        except:
            print('Please, write a number')
    funk_result2() #result   (operand1 operator operand2)




print(result)



















