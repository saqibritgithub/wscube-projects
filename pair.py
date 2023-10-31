from collections import Counter

l1 = [2, 3, 4, 4, 5, 6, 5, 5, 4, 2, 2, 2]
number_count = Counter(l1)
total_pairs = 0
for count in number_count.values():
    total_pairs += count // 2
print("Total count of pairs:", total_pairs)
