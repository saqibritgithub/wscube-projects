s = "pwwkew"
max_length = 0
b = 0
a = {}

for i in range(len(s)):

    if s[i] in a and a[s[i]] >= b:
        b = a[s[i]] + 1
    a[s[i]] = i
    max_length = max(max_length, i - b + 1)

print(max_length)