nums = [1, 2, 3, 1]

for i in range(1, len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        print("Peak element found at index:", i)
        break
else:
    if nums[0] > nums[1]:
        print("Peak element found at index: 0")
    elif nums[-1] > nums[-2]:
        print("Peak element found at index:", len(nums) - 1)

