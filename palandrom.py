s = "babd"
max_palindrome = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j+1]
        if substring == substring[::-1] and len(substring) > len(max_palindrome):
            max_palindrome = substring

print(max_palindrome)
