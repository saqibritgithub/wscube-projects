import random

lst = [1, 2, 3, 4, 9, 8, 5]
m = random.choice(lst)
a = []

user_choice = int(input('''
Please enter what you want...
    1: Return a single value
    2: Return two min numbers
'''))

if user_choice == 1:
    s = int(input("Please enter the number you want to return: "))
    print(s)
    exit()
if user_choice == 2:
    check = int(input("Please enter a number you want to check: "))

    for element in lst:
        if m<check:
            d = element + m
            if d == check:
                a.append(element)
                a.append(m)


    print("a:", a)
