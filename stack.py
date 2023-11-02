def push(num,n):
    num.append(n)
    return num
def pop(num):
    if isempty(num):
        print("The list is empty")
        return False
    else:
        num.pop()
        return num
def isempty(num):
    if not num:
        return True
    else:
        return False
num=[]
push(num,3)
push(num,5)
push(num,6)
push(num,3)
pop(num)
isempty(num)

print(num)
print(isempty(num))
