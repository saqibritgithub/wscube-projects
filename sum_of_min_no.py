import random

lst = [1, 2, 3, 4, 9, 8, 5]
m = random.choice(lst)
a = []

user_choice = int(input('''
Please enter what you want...
    1: Return a single value
    2: Return pairs of numbers whose sum equals a random number
'''))

if user_choice == 1:
    s = int(input("Please enter the number you want to return: "))
    print(s)
    exit()
if user_choice == 2:
    check = int(input("Please enter a number you want to check: "))

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == check:
                a.append((lst[i], lst[j]))
print(max(a))

