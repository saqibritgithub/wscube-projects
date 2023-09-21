import random
coins = int(input("Please enter the number of coins you want to return: "))
s = [10, 5, 2, 1]
a = []
while coins > 0:
    max_coin = max([coin for coin in s if coin <= coins])
    a.append(max_coin)
    coins -= max_coin
print("Coins to return:", a)
print("the coin 10 is used =",a.count(10),"times")
print("the coin 5 is used =",a.count(5),"times")
print("the coin 2 is used =",a.count(2),"times")
print("the coin 1 is used =",a.count(1),"times")