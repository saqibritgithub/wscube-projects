num=int(input("enter any number: "))
s=[]
v=num%10
l=num//10
s.append(v)
s.append(l)
if len(s)>=2 and s[0]+s[1]<10:
    s=s[0]+s[1]
    if s<10:
        print(s)
else:
    s=s[0]+s[1]
    q=s%10
    w=s//10
    s=[]
    s.append(q)
    s.append(w)
    s=s[0]+s[1]
    print(s)

