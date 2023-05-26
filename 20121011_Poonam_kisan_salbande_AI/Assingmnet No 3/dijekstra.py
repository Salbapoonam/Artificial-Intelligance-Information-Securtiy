import heapq

def dijkstra(graph, source):
    dist = [float('inf')] * len(graph)   # list to store the shortest distance from the source to each vertex
    visited = [False] * len(graph)       # list to keep track of visited vertices
    heap = [(0, source)]                 # heap to store the vertices to visit, with the current distance from the source
    dist[source] = 0                     # distance from the source to itself is 0
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(heap, (alt, v))
    return dist

# Example input
graph = [[(1, 2), (2, 4)],      # edges from vertex 0 to vertex 1 and 2 with weights 2 and 4, respectively
         [(0, 2), (2, 3), (3, 2)],  # edges from vertex 1 to vertex 0, 2, and 3 with weights 2, 3, and 2, respectively
         [(0, 4), (1, 3), (3, 1)],  # edges from vertex 2 to vertex 0, 1, and 3 with weights 4, 3, and 1, respectively
         [(1, 2), (2, 1)]]      # edges from vertex 3 to vertex 1 and 2 with weights 2 and 1, respectively
source = 0

# Run the algorithm and print the result
dist = dijkstra(graph, source)
print("Shortest distances from vertex", source, "to all other vertices:", dist)
