#a="true"
#b="false"
#print(a+" "+b)
#a="10"
#b="moon"
#print(a+b)
#string slicing
#print(a[0:7:2])
#print(a[0::])
#string iteration
#for a in range(w):
 #   print(t[a])
#reverse iteration
###print(b)
#for r in range(b-1,-1,-1):
    #print(a[r])
    #string functions
#print(s)
#######print(j.find('c',3))
#print(j.index(""))
#h="welcome"
#print(h.isalpha())
#k="145"
#print(k.isdigit())
#a=65;
#print(chr(67))
#a="A"      #capital a start from 65 and small a start from 97
#print(ord(a))
#g="a"
#print(ord(g))
##s=len(f)
#print(s)
#for a in range(s):
 #   print(f[a])
    #1
my_string = ""
t="pwwkew"
w=len(t)
print(w)
for a in range(w):
    s=(t[a])
    if s not  in my_string and s!="p":
        my_string += s
        print(s, end="")

#2
my_string = ""
t="abcabcbb"
w=len(t)
print(w)
for a in range(w):
    s=(t[a])
    if s in my_string:
        break
    else:
        my_string+=s
    print(s,end="")
#3
my_string = ""
t="bbbb"
w=len(t)
print(w)
for a in range(w):
    s=(t[a])
    if s in my_string:
        break
    else:
        my_string+=s
    print(s,end="")


