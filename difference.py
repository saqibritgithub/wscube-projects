numbers = [7, 2, 3, 10, 2, 4, 20, 1]
numbers.sort(reverse=True)
print(numbers)

if len(numbers) < 2:
    print("your list can not contain only one element; ")
else:
    differences = []

    for i in range(len(numbers) - 1):
        diff = numbers[i] - numbers[i+1]
        differences.append(diff)

    print("the maximum difference between these numbers is ;",max(differences) )
