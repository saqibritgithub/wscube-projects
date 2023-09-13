#range
range(5)
#start=0
#condition<5
#incremint=1by default
range(4,12)
#start=4
#condition<12=11
#incremint=1
range(2,7,2)
#start=2
#condetion<7=6
#increment=2
for c in range(7):
    print("moon")
    #reverse lop
for x in range(10,1,-1):
    print(x)
#table of two
for c in range(1,11):
    print("2 *",c,"=",c*2)
    #table of three
for c in range(1,11):
    print("3 *",c,"=",c*3)

    i=i+1
    num=int(input("enter the number to chech for prime no"))
    j=0
    while(i<num):
        if(num%i==0):
            j=j+1
            i=i+1
            if(j==2):
             print(i)
