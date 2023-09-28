a=int(input("enter the vale to find the square root: "))
l=[]
for i in range(a):
    if i*i==a:
        print(i)
        break
else:
    if i*i!=a:
        for i in range(a):
            if i*i<a:
                l.append(i)
            elif i*i>a:
                break
print(max(l))