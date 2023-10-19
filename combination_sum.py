#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]
#Explanation:
#2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#7 is a candidate, and 7 = 7.
#These are the only two combinations
candidates=[2,3,4,5]
target=int(input("plz enter targer value :"))
for i in range(len(candidates)):
    for j in range(len(candidates)):
        if(candidates[i])+(candidates[j])==target:
            s=(candidates[i],candidates[j])
            break
print(s)

