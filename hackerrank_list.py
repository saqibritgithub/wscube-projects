lst=[]
n=int(input())
for i in range (n):
    command=input().split()
    if command[0] == 'insert':
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)
    elif command[0]=='print':
        print(lst)
    elif command[0]=='remove':
        lst.remove(int(command[1]))
    elif command[0]=='append':
        lst.append(int(command[1]))
    elif command[0]=='sort':
        lst.sort()
    elif command[0]=='pop':
        lst.pop()
    else:
        lst.reverse()