s = "adhjassd"
unique_chars = ""

for char in s:
    if char not in unique_chars:
        unique_chars += char

print(unique_chars)


