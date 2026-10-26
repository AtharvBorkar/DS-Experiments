# Adjacency Matrix (for DFS)
matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

nodes = ['A', 'B', 'C', 'D', 'E']

def dfs(matrix, start, visited=None):
    if visited is None:
        visited = set()
    print(nodes[start], end=' ')
    visited.add(start)
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and i not in visited:
            dfs(matrix, i, visited)

# Adjacency List (for BFS)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("DFS Traversal (Adjacency Matrix):")
dfs(matrix, 0)
print("\nBFS Traversal (Adjacency List):")
bfs(graph, 'A')