# def fnc(n):
#     if n == 3:
#         return 3
#     return fnc(n-1)+n

# result = fnc(5)
'''
    3/14
'''
# def format_ingredients(items):
#     words = ''
#     for i in items:
#         if len(items) < 2:
#             words += i
#         elif i != items[-1] and i != items[-2]:
#             words += i + ',' + ' '
#         elif i == items[-2]:
#             words += i + ' '
#         else:
#             words += 'and' + ' ' + i
#     return words


'''
    4/14
'''


# def get_grade(key):
#     a = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
#     return a.get(key)


# def get_description(key):
#     b = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
#          "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
#     return b.get(key)


'''
    5/14
'''


# def lookup_key(data, value):
#     new = []
#     new = data.copy()
#     print(new)

#     if new != 2:
#         print(['key2', 'key4'])


'''
    6/14
'''

# def split_list(grade):
    
#     whole_numbers = []
#     whole_numbers_top = []
    
    
#     if len(grade) == 0:
#         return whole_numbers, whole_numbers_top
#     else:
#         average = sum(grade) / len(grade)
#         for el in grade:
#             if el > average:
#                 whole_numbers_top.append(el)
#             else:
#                 whole_numbers.append(el)
#         return whole_numbers, whole_numbers_top


'''
    10/14
'''




# from random import randint

# def get_random_password():

#     N = 8
#     password = ""

#     for _ in range(N):
        
#         random_num = randint(40, 126)
        
#     return password
        

# get_random_password()



# import string
# import random
# from random import randint


# def get_random_password():
    
#     random_num = randint(40, 126)

#     return random_num


# print("Вывод случайного целого числа ", randint(0, 9))


# N = 20  # password length

# # allowed string constants
# allowedChars = string.ascii_letters + string.digits + string.punctuation

# # genereate password
# password = ''.join(random.choice(allowedChars) for _ in range(N))

# print(password)


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
#         encoded_message += ch


'''
    11/14
'''
# def is_valid_password(password):

#     has_lit = False
#     has_big = False
#     has_num = False

#     if len(password) < 8:
#         return False
#     for i in password:
#         char_as = ord(i)
#         if 48 <= char_as <= 57:
#             has_num = True
#         elif 65 <= char_as <= 90:
#             has_big = True
#         elif 97 <= char_as <= 122:
#             has_lit = True

#     return has_lit and has_big and has_num


'''
    12/14
'''

# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result


# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False


# def get_password():
#     for i in range(100):
#         password = get_random_password()
#         if is_valid_password(password):
#             return password


'''
    13/14
'''


# from pathlib import Path

# def parse_folder(path):
    
#     files = []
#     folders = []
#     path = Path(path)
#     dir_path = path.iterdir()
#     for i in path.iterdir():
#         if i.is_file():
#             files.append(i.name)
#         elif i.is_dir():
#             folders.append(i.name)
    
#     return files, folders


# parse_folder("/home")


'''
    14/14
'''

# import sys


# def parse_args():
#     result = sys.argv[1] + " " + sys.argv[2]

#     return result


# import sys
# for arg in sys.argv:
#     print(arg)
