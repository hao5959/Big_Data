graph =  {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

# def bfs(graph, root):
#     res = []
#     queue = [root]
#     # keep looping until there are nodes still to be checked
#     while queue:
#         node = queue.pop(0)
#         if node not in res:
#             res.append(node)
#             next_row = graph[node]
#             for next in next_row:
#                 queue.append(next)
#     return res

# print(bfs(graph, 'A'))
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
bfs(visited, graph, 'A')
# ==============================================================
#return parent relation
# def bfs(graph, root):
#     visited = set()
#     visited.add(root)
#     queue = [root]
#     parent = {root: None}
# ==============================================================

# find the shortest path
def bfs_hortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal: return 'you got it'
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbors not in explored:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == goal:
                        return print(new_path)
            explored.append(node)
    return 'sorry, no connecting path'
bfs_hortest_path(graph, 'G', 'D')