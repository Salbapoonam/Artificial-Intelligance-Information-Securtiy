
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

# Recursive depth-first search function
def dfs(graph, vertex, visited):
    # Mark the current vertex as visited
    visited.add(vertex)
    print(vertex, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Driver code
visited = set()  # Set to keep track of visited vertices
for vertex in graph:  # For each unvisited vertex, call dfs
    if vertex not in visited:
        dfs(graph, vertex, visited)
