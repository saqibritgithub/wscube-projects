user_choice=int(input("""
    plz select the gender of human:
    1. MALE
    2. FEMALE
    """))
if user_choice==1:
    age=int(input("plx enter the age of a man : "))
    if(age>=25 and age<=28):
        print("Congratulations this man can apply for the job")
    else:
        print("invalid operation")
elif user_choice==2:
    age = int(input("plx enter the age of this woman : "))
    if (age >= 25 and age <= 32):
        print("Congratulations this lady can apply for the job")
    else:
        print("invalid operation")
else:
    print("sorry, i think you did not select the right choice")

