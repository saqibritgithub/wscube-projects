l = [9,9,9]
v = int(input("Please enter the number you want to add: "))

for i in range(1, len(l) + 1):
    s = l[-i] + v

    if s >= 10:
        r = s % 10
        l[-i] = r
        v = s // 10
    else:
        l[-i] = s
        break

if v > 0:
    l.insert(0, v)

print(l)
