def add_node(v):
    global count
    if v in nodes:
        print(v,"This node is already present in graph")
    else:
        count=count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(count):
            temp.append(0)
        graph.append(temp)
def print_graph():
    for i in range(count):
        for j in range(count):
            print(graph[i][j],end="")
        print()
nodes=[]
graph=[]
count=0
print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
print("After adding nodes")
print(nodes)
print(graph)
print_graph()