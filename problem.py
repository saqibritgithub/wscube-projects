string="BANANA"
vowels="A,E,I,O,U"
v=""
for i in range(len(string)):
    if string[i]  in vowels:
        for j in range(len(string[i:])):
            v+=string[j]
            print(v)

