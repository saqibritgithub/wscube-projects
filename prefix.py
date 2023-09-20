str = ["flower", "floew", "flowight"]
if not str:
    common_prefix = ""
else:
    shortest_str = min(str, key=len)
    for i, char in enumerate(shortest_str):
        for string in str:
            if string[i] != char:
                common_prefix = shortest_str[:i]
                break
        else:
            continue
        break
    else:
        common_prefix = shortest_str

print(common_prefix)
