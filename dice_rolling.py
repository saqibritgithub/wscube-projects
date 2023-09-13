import random
again=True
while again:
    print(random.randint(1,6))
    another_roll=input("want to roll again yes/no :")
    if another_roll.lower()=="yes":
        continue
    else:
        break