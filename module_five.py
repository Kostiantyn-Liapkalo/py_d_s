# """
#     1/15
# """
 
# import re
 
# text = 'Alex\nKdfe23\t\f\v.\r'


# def real_len(text):
#     fu = re.split(r'\w', text)
#     return len(fu)


# real_len(text)


# """
#     2/15
# """

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


# """
#     5/15
# """


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


# """
#     6/15
# """
  
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
    
    
      
    
        
        
        
            
        
        
            
        
        
            
        
        
            
        
            
    
    







    