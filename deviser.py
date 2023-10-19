#Input: dividend = 10, divisor = 3
#utput: 3
#Explanation: 10/3 = 3.33333.. which is truncated to 3.
dividend=int(input("plz enter the vlaue of dividend ;"))
divisor=int(input("plz enter the vlaue of divisor ;"))
result=0
if dividend%divisor==0:
    for i in range(1,dividend):
        result+=divisor
        if result==dividend:
            break
    print(i)
else:
    for i in range(1,dividend):
        result+=divisor
        if result>=dividend:
            break
    print(i-1)



