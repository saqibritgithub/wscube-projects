#
#j="welcome to moons era"
#
#print(j.find('c'))

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#t="abcabcbb"
#v={}
#w=len(t)
#print(w)
#for a in range(w):
# Create an empty string
my_string = ""
t="abcabcbb"
w=len(t)
print(w)
for a in range(w):
    s=(t[a])
    if s in my_string:
        break
    else:
        my_string+=s
    print(s,end="")
#my_string = ""

# Add a specific alphabet to the empty strin
#alphabet_to_add = "X"  # Change "X" to the alphabet you want to add
#my_string += alphabet_to_add

# Now my_string contains the specified alphabet
#print(my_string)
#t="abcabcbb"
#w=len(t)
#print(w)
#for a in range(w):
    #print(t[a])
