a = ["flower", "floow", "floght"]

prefix=("")


string1 = a[0]
string2 = a[1]
string3 = a[2]
s=min(string1,string2,string3,key=len)



if s[0]==string2[0] and s[0]==string3[0]:
    prefix+=s[0]
    if s[1] == string2[1] and s[1] == string3[1]:
            prefix += (s[1])
    if s[2] == string2[2] and s[2] == string3[2]:
        prefix += s[2]

    print(prefix)
else:
    print("()")









