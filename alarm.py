#BAR GRAPH
import matplotlib.pyplot as plt
plt.bar([2,4,6,8,5],[1,3,5,7,9],label="example1")
plt.bar([3,4,5,3,7],[2,3,5,7,9],label="example2",color="g")
plt.legend()
plt.xlabel("Bar_Number")
plt.ylabel("Bar_height")
plt.title("Info")
plt.show()
#histograph to show population differences
population=[23,44,35,37,47,45,34,35,48,49,47,36,35,53,4,35,36]
Bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population,Bins,histtype="bar",rwidth=0.8)
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.legend()
plt.show()


