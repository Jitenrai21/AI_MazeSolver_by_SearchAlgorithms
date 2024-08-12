from collections import deque

maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1]
]
start = (0, 1)
goal = (4, 3)

# def get_neighbors(maze, row, col):
#     neighbors = []
#     rows, cols = len(maze), len(maze[0])

#     directions = [(-1, 0), (1,0), (0,-1), (0,1)]

#     for dr, dc in directions:
#         new_row, new_col = row + dr, col + dc

#         if 0<=new_row < row and 0 <= new_col < col and maze[new_row][new_col] == 0:
#             neighbors.append((new_row, new_col))
#     return neighbors

# def reconstruct_path(parent, start, goal):
#     path = []
#     current = goal

#     while current != start:
#         path.append(current)
#         current = parent[current]

#     path.append(start)
#     path.reverse()

#     return path

def dfs(maze, start, goal):
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        current = stack.pop()
        row, col = current

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        if current not in visited:
            visited.add(current)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    neighbor = (new_row, new_col)
                    if neighbor not in visited:
                        parent[neighbor] = current
                        stack.append(neighbor)

    return None  


# def dfs(maze, start, goal):
#     stack = [start]
#     visited= set()
#     parent = {}

#     while stack:
#         current = stack.pop()

#         if current in visited:
#             continue

#         visited.add(current)

#         if current == goal:
#             break

#         row, col = current
#         neighbors = get_neighbors(maze, row, col)

#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 stack.append(neighbor)
#                 parent[neighbor] = current

#     return reconstruct_path(parent, start, goal)

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (row, col), path = queue.popleft()

        if (row,col) == goal:
            return path
        
        if (row, col) not in visited:
            visited.add((row, col))

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    queue.append(((new_row, new_col), path + [(new_row,new_col)]))
    return None

path = bfs(maze, start, goal)
print(path)
