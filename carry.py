
l=[7,4,7,5,3,4,7,5]
v=int(input(" plz select the no. you want to add ;"))
for i in range (1,len(l)+1):
    s=l[-i]+v
    if s>=10:
        r=s%10

        l[-i]=r
        v=s//10



    elif s<10:
        l[-i]+=v
        break


print(l)