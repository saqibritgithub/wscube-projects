nums = [4,3,4]
nums.sort(reverse=True)
str_nums = [str(num) for num in nums]

result_string = ''.join(str_nums)
print(result_string)