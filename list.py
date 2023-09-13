#list slicing
a=[1,2,3,4,5,["gello",4,5,5,[1,2,3,4]]]
print(a[2])
print(a[2: :2])
print(a[2])
print(a[5])
print(a[-1])
#list functions
#count
f=[23,3,32,24,23,45,32]
j=f.count(23)
print(j)
#max
f=[2,3,4,5,6,7,8]
s=max(f)
print(s)
#min
f=[4,63,4,4]
s=min(f)
print(s)
#reverse
d=[3,3,5,3,24,6,7,5,4]
d.reverse()
print(d)
#sort
f=[2,2,6,5,4,5,4]
f.sort()
print(f)
#zip function to iterate two lists at the same time
f=[12,2,32,23]
l=[4,3,4,3,2]
for a,v in zip(f,l):
    print(a,v)
#split function to  convert string into list
a=(input("enter any string you want"))
f=a.split()
print(f)
#append function to convert more inputs to string
s=[]
for a in range(1,4):
    n=(input("enter the value 1 : "))
    s.append(n)
print(s)
# lifo:last in first oout
# filo:first in last out
# functions to add delete display list
l=[]
while True:

    n=int(input('''
    1,pop element
    2,push element
    3,peak element
    4display element'''))
if n == 1:
    c = input("enter any value");
    l.append(c)
    print(l)
elif n==2:
    if len(l)==0:
        print("empty list")
    else:
        t=l.pop()
        print(t)

elif n==3:
    print("peak element",l[-1])




