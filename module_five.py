
 
# import re
 
# text = 'Alex\nKdfe23\t\f\v.\r'


# def real_len(text):
#     fu = re.split(r'\w', text)
#     return len(fu)


# real_len(text)




# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]


# def find_articles(key, letter_case=False):
    

#     result = []
    
#     for article in articles_dict:
#         for _,value in article.items():
#             if letter_case:
#                 if key in str(value):
#                     result.append(article)
#                     break
#             else:
#                 if key.upper() in str(value).upper():
#                     result.append(article)
#                     break
#     return result
           
           
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone




# def get_phone_numbers_for_countries(list_phones):

#     numbers_for_countries = {
#         "UA": [],
#         "JP": [],
#         "TW": [],
#         "SG": []
#     }
#     sanitize_phone = sanitize_phone_number("/".join(list_phones)).split("/")
#     print(sanitize_phone)
#     for phone in sanitize_phone:
#         if phone.startswith('81'):
#             numbers_for_countries["JP"].append(phone)
#         elif phone.startswith('886'):
#             numbers_for_countries["TW"].append(phone)
#         elif phone.startswith('65'):
#             numbers_for_countries["SG"].append(phone)
#         else:
#             numbers_for_countries["UA"].append(phone)
#     print(numbers_for_countries)
#     return numbers_for_countries

  
# import re  
  
  
# text = 'Молох бог ужасен.'
# spam_words = ['лох',]


# def is_spam_words(text, spam_words, space_around=False):

#     text_new = text.lower()

#     for word in spam_words:
#         spam = word.lower()
#         if space_around:
#             if re.findall(r'[\s]{1}' + spam + r'\s?', text_new):
#                 return True
#             return False
#         elif text_new.find(spam):
#             return True
        


# is_spam_words(text, spam_words, True)
    

# 


# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
#                "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()

# name = "Олекса Івасюк"

# def translate(name):

#     translated_name = ""

#     for let in name:
#         if TRANS.get(ord(let)):
#             translated_name += TRANS[ord(let)]
#         else:
#             translated_name += let
#     return translated_name


# translate(name)
            

            
# width = 5
# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))


# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


# def formatted_grades(students):

#     num = 1
#     s = ''
#     result = []
#     for name, grade in students.items():
#         s = '{:>4}|{:<10}|{:^5}|{:^5}'.format(
#             num, name, grade, grades.get(grade))
#         num += 1
#         result.append(s)
#     return result


#

# def formatted_numbers():
#     numbers = []
#     numbers.append('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))
#     for i in range(0, 16):
#         numbers.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))
#     return numbers



   