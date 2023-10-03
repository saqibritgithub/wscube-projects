# Given list and target integer
my_list = [2,3,5,7,8]
my_target = 8


for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] + my_list[j] == my_target:
            print("The pair with sum",my_target,"is :",(my_list[i],my_list[j]))
            break

