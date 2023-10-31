def sum(a,b):
    print(a+b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a-b)
sum(12,23)
#math functions
#math.ceil(change float valur to next integers value)
#math.fab(return the absolute value)
import math
x=12.6
t=-12
print(math.ceil(x))
print(math.fabs(t))
#math.factorial(x)
import math
x=5
print(math.factorial(x))
#math.floor(remove values after point)
x=6.56
print(math.floor(x))
#math.fsum(displlay the sum of whole list)
x=[5,5,6,5,6,3,6]
print (math.fsum(x))
#math.sqrt(for square root of integers)
print(math.sqrt(49))
#have different pair of socks we have to return nu. of pairs of same colour
def sum(a,b):
    print(a+b)
sum(4,5)
def even(s):
    if s%2==0:
        print("the entered no. is even")
    else:
        print("the entered no. is odd")
even(3)
def factorial(s,u):
    for i in range(1,s):
        u*=i
    print(u)
factorial(6,1)
def largest(l):
    print(max(l))
l=[2,3,4,4,5,5,6,7,8,9]
largest(l)
def double_char(a,v=""):
    for char in a:
        v+=char*2
    print(v)
a="asdf"
double_char(a)
