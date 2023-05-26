

# Implement bredth  first search algorithm  use an
# undirected graph and develop a recursive algorithm for searching all the vertices of a graph
# or tree data structure.


# Undirected graph representation using adjacency list
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A', 'E', 'F'],
    'E': ['D'],
    'F': ['D']
}

# Breadth-first search (BFS) algorithm
def bfs(start_vertex):
    visited = set()
    queue = [start_vertex]
    visited.add(start_vertex)
    
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Depth-first search (DFS) algorithm
def dfs(vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# Call BFS and DFS on the graph
start_vertex = 'A'
print('BFS traversal:')
bfs(start_vertex)
print()
print('DFS traversal:')
visited = set()
dfs(start_vertex, visited)
