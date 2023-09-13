import random
computer_num=random.randrange(1,100)
user_num=int(input("enter any number you want a;"))
if computer_num>user_num:
    print("your enterd no is low ;")
elif computer_num<user_num:
    print("your enterd no is high ;")
elif computer_num==user_num:
    print("well gauessed ;")
else:
    print("invalid operation")
