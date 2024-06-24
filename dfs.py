graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]    
}

visited=[]
queue=[]

def bfs(visted,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop()
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth First Search")
bfs(visited,graph,'5')

# def dfs(graph,visited,node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         m=queue.pop()
#         print(m,end=" ")

#         for neighbour in graph[m]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)

# def create_graph():
#     graph={}
#     num_node=int(input("Enter the number of nodes"))

#     for  _ in range(num_node):
#         node=input("Enter the node")
#         neighbour=input(f"Enter the neighbours of node {node}").split()
#         graph[node]=neighbour

#     return graph

# print("Create a graph")
# graph=create_graph()
# print("\n")
# print(graph)
# visited=[]
# queue=[]
# node=input("enter the node")
# dfs(graph,visited,node)


