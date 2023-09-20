a = []
brackets = {')': '(', '}': '{', ']': '['}
s = input("enter the bracket you want to check : ")

for char in s:
    if char in brackets.values():
        a.append(char)
        print(a)
    elif char in brackets.keys():
        if not a or a.pop() != brackets[char]:
            print(False)
            break
else:
    print(not a)





