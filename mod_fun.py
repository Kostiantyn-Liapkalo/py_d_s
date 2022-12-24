


# def trip_price(path):
#     global total_trip
#     total_trip += 1
#     sum_trip = base_rate + price_per_km * path
#     return (sum_trip)

# prise_dascount


# def discount_price(price, discount):
#     price -= price * discount

#     def apply_discount():

#         nonlocal price

#     apply_discount()
#     return price


# firstname = input("What is your first name?")
# lastname = input("What is your last name?")
# fullname = firstname + lastname
# currentyear = 2022
# birthyear = input("What year were you born? ")
# ibirthyear = int(birthyear)
# age = currentyear - ibirthyear
# print("Welcome " + fullname, age)



# def greet(name, *args):
#     for n in (name,) + args:
#         print(f'Hello, {n}!')


# greet('Tom', 'Ann')




# print(globals())


# def first(size, *args):
#     return size + len(args)


# def second(size, **qwargs):
#     return size + len(qwargs)


# s = 0
# try:
#     s += 1/0
# except ZeroDivisionError:
#     s += 1
# else:
#     s += 5
# finally:
#     s += 10
# print(s)


# def cost_delivery(quantity, *_, discount=0):
#     if discount >= 0 or discount == 1:
#         if quantity >= 1:
#             result = (quantity - 1) * 2 + 5
#             result = result - result * discount
#         else:
#             discount = 0
#     else:
#         raise Exception("Less 0 or 1!")
#     return result


# def cost_delivery(quantity, *_, discount=0):
#     """Функція повертає суму за доставлення замовлення.

#      Перший параметр &mdash; кількість товарів в замовленні.
#      Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result


# print(cost_delivery.__doc__)




# # Function for nth Fibonacci number
# def Fibonacci(n):

#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")

#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0

#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1

#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)


# # Driver Program
# print(Fibonacci(9))


# def Fibonacci(n):
#     lis=[1, 1]
#     for i in range(n-2):
#         lis.append(lis[-1] + lis[-2])
#     return lis[-1]


# def Fibonacci(n): return 1 if n<=2 else Fibonacci(n-1) + Fibonacci(n-2)

# if n <= 2:
#     return 1
# return Fibonacci(n-1) + Fibonacci(n-2)


#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(20))


