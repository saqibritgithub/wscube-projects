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
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"This node is not present in the graph")
    elif v2 not in nodes:
        print(v2,"This node is not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"This node is not present in the graph")
    elif v2 not in nodes:
        print(v2,"This node is not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def print_graph():
    for i in range(count):
        for j in range(count):
            print(graph[i][j],end="")
        print()
nodes=[]
graph=[]
count=0
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",5)
print(graph)
print_graph()

