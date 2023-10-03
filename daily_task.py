s = int(input("plz enter the number you want to reverse: "))
v = int(str(s)[::-1]) * (-1 if s < 0 else 1)
print(v)
