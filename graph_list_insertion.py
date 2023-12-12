def add_node(v):
    if v in nodes:
        print(v,"This node is alredy present" )
    else:
        nodes[v]=[]
def add_edge(v1,v2,cost):
    if v1 not  in nodes:
        print(v1,"This node is already present")
    elif v2 not  in nodes:
        print(v2,"This node is already present")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        nodes[v1].append(list1)
        nodes[v2].append(list2)
#directed and waited
def add_edg(v1,v2,cost):
    if v1 not  in nodes:
        print(v1,"This node is already present")
    elif v2 not  in nodes:
        print(v2,"This node is already present")
    else:
        list1=[v2,cost]
        nodes[v1].append(list1)

nodes={}
add_node("A")
add_node("B")
add_node("C")
add_edg("A","C",10)
print(nodes)