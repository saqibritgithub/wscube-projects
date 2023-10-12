num1 = input("plz enter the first value : ")
num2 = input("plz enter the second vlaue : ")

result = 0

for i in range(len(num1)):
    for j in range(len(num2)):
        result += int(num1[i]) * int(num2[j]) * (10**(len(num1) + len(num2) - i - j - 2))
result_str = str(result)
print(result_str)

