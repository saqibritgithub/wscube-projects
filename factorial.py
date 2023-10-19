n=int(input("plx enter the number you want t0 find factorial ;"))
factorial=1
for i in range(1,n):
    factorial+=factorial*i
print(factorial)
if (factorial % 10) == 0:
    string=str(factorial)
    zeroes=string.count("0")
    print(zeroes, "trailing zeroes")
else:
    print("no trailing zero")

