#have different pair of socks we have to return nu. of pairs of same colour
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
l1=[9,9,9,9,9,9,9]
l2 = [9,9,9,9]
y=[]
z=[]
t=[]

for i in range(1,len(l1)+1):
    y.append(l1[-i])
for i in range(1,len(l2)+1):
    z.append(l2[-i])
num1 = int("".join(map(str, y)))
num2 = int("".join(map(str, z)))
result=num1+num2
digit_list = [int(digit) for digit in str(result)]
for i in range(1,len(digit_list)+1):
    t.append(digit_list[-i])
print(t)


