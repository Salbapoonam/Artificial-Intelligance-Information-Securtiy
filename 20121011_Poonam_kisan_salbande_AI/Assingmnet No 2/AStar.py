import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(start, goal, grid):
    open_list = []
    closed_list = []
    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == goal:
            path = []
            while current_node.parent:
                path.append(current_node)
                current_node = current_node.parent
            path.append(current_node)
            return path[::-1]

        neighbors = []
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_x = current_node.x + i
            neighbor_y = current_node.y + j
            if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]) and grid[neighbor_x][neighbor_y] != 1:
                neighbors.append(Node(neighbor_x, neighbor_y))

        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            tentative_g = current_node.g + 1
            if tentative_g < neighbor.g:
                neighbor.parent = current_node
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)

    return None

grid = [[0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0]]

start = Node(0, 0)
goal = Node(3, 3)

path = astar(start, goal, grid)

if path:
    for node in path:
        print(f"({node.x}, {node.y})")
else:
    print("No path found.")
