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
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth First Search")
bfs(visited,graph,'5')


# def create_graph():
#     graph={}
#     num_node=int(input("Enter the number of nodes"))
#     for _ in range(num_node):
#         node=input("Enter the node")
#         neighbour=input("Enter its neighbours").split()
#         graph[node]=neighbour
    
#     return graph

# def bfs(graph,node):
#     visited=[]
#     queue=[]
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         m=queue.pop(0)
#         print(m,end=" ")
    
#         for neighbour in graph[m]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)

# graph=create_graph()
# node=input("Enter the node to start")
# print("The bfs is ")
# bfs(graph,node)

# def create_graph():
#     graph = {}
#     num_nodes = int(input("Enter the number of nodes: "))
#     for _ in range(num_nodes):
#         node = input("Enter the node: ")
#         neighbors = input(f"Enter its neighbors: ").split()
#         graph[node] = neighbors
#     return graph

# def bfs(graph, start_node):
#     visited = []
#     queue = []
#     paths = {}

#     visited.append(start_node)
#     queue.append(start_node)
#     paths[start_node] = [start_node]

#     while queue:
#         current_node = queue.pop(0)
#         print(current_node, end=" ")

#         for neighbor in graph[current_node]:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 queue.append(neighbor)
#                 paths[neighbor] = paths[current_node] + [neighbor]

#     return paths

# print("Enter the graph")
# graph = create_graph()
# start_node = input("Enter the node to start: ")

# paths = bfs(graph, start_node)
# print("\nPath from start to end:")
# for node in paths:
#     print(f"{start_node} to {node}: {' -> '.join(paths[node])}")
