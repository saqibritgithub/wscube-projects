#

l=[2,3,5,6,5,9]
v=int(input("enter ;"))
for i in range (1,len(l)):
    s=l[-i]+v
    if s>=10:
        r=s%10
        print(r)

        l[-i]=r
        v=s//10


    elif s<10:
        l[-i]+=v
        break


print(l)