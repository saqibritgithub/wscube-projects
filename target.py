nums = [1,3,5,6]
target=2
for i in range(len(nums)):
    if nums[i]==target:
        print(i)
        break

else:
    for i in range(len(nums)):
        if nums[i] >= target:
            print(i)
            break



