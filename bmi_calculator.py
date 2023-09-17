h=float(input("enter your height in cm :"))
w=float(input("enter your weight in kilograms :"))
bmi=w/(h/100)**2
print("your calculated bmi is :" , bmi)
#now apply some conditions on this
if bmi <=18.4:
    print("you are underweight kux khaya kr gr walay khana nhi daitay kya ")
elif bmi <=24.9:
    print ("you are health person congratulations zindgi enjoy kro  ")
elif bmi <=29.9:
    print ("omg you are overweight kam khaya kr")
elif bmi <=34.9:
    print ("you are very obess motay honay ka zayada shoq h jaldi mr jao gy")
elif bmi <=39.9:
    print ("you are very very faty what is your last wish  because you are about to  die")
else:
    print("danger")