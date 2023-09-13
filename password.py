import random
character="qwertyuioplkjhgfdsazxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP123456789!@#$%^&*_"
pass_length=int(input("enter the length of your password :"))
pass_count=int(input("enter the no. of passwords you want :"))
for i in range(0,pass_count):
    password=""
    for j in range(0, pass_length):
        password_char=random.choice(character)
        password=password_char+password
    print("your generated password is :",password)


