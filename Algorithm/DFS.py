graph = {
    "A":["B", "C"],
    "B":["A", "C", "D"],
    "C":["A", "B", "D", "E"],
    "D":["B", "C", "E", "F"],
    "E":["C", "D"],
    "F":["D"]
 }

def dfs(graph, root):
    queue = [root]
    visited = set()
    visited.add(root)
    while queue:
        vertex = queue.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        print(vertex)

dfs(graph, 'A')

# ========================================
# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

# visited = set() # Set to keep track of visited nodes.

# def dfs(visited, graph, node):
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# # Driver Code
# dfs(visited, graph, 'A')