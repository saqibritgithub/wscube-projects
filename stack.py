#exploring stack data structure
stack=[]
def push():
    e=int(input("plz enter the no. to push in stack:"))
    stack.append(e)
    print(stack)
def pop():
    if not stack:
        print("The stack is empty")
    else:
        e=stack.pop()
        print(e)
while True:
    choice=int(input('''
        1: push
        2: pop
        2: quit
    '''))
    if choice==1:
        push()
        print(stack)
    if choice==2:
        pop()
        print(stack)
    if choice==3:
        break
    else:
        print("incorrect operation")

