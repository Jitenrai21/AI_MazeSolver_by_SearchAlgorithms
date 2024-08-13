
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1]
]
start = (0, 1)
goal = (4, 3)

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

from collections import deque

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

import heapq

def ucs(maze, start, goal):
    pq = [(0, start, [start])] #here, cost = 0, (row,col) = start, path= [start]
    visited = set()

    while pq:
        cost, (row, col), path = heapq.heappop(pq)

        if (row, col) == goal:
            return path
        
        if(row, col) not in visited:
            visited.add((row, col))

            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    new_cost = cost + 1
                    heapq.heappush(pq, (new_cost, (new_row, new_col), path + [(new_row, new_col)]))
    return None

def manhattan_distance (point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def a_star(maze, start, goal):
    pq = [(manhattan_distance(start, goal), 0, start, [start])]
    visited = set()

    while pq:
        f, cost, (row, col), path = heapq.heappop(pq)

        if (row, col) == goal:
            return path
        
        if (row, col) not in visited:
            visited.add((row, col))
        
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    new_cost = cost + 1
                    h = manhattan_distance((new_row, new_col), goal)
                    heapq.heappush(pq, (new_cost + h, new_cost, (new_row, new_col), path + [(new_row, new_col)]))

    return None


def best_first_search(maze, start, goal):
    pq = [(manhattan_distance(start, goal), start, [start])]
    visited = set()

    while pq:
        h, (row, col), path = heapq.heappop(pq)

        if (row, col) == goal:
            return path
        
        if (row, col) not in visited:
            visited.add((row, col))

            directions = [(-1,0), (1, 0), (0,-1), (0,1)]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    heapq.heappush(pq, (manhattan_distance((new_row, new_col), goal), (new_row, new_col), path + [(new_row, new_col)]))

    return None

def choose_algorithm():
    print("Select a search algorithm:")
    print("1. Depth First Search (DFS)")
    print("2. Breadth First Search (BFS)")
    print("3. Uniform Cost Search (UCS)")
    print("4. A* Search")
    print("5. Best-First Search")

    choice = input("Enter the number for your choosen algorithm: ")

    if choice == '1':
        return dfs
    elif choice == '2':
        return bfs
    elif choice == '3':
        return ucs
    elif choice == '4':
        return a_star
    elif choice == '5':
        return best_first_search
    else:
        print("Invalid choice. Please choose from one of the available search algorithm choice.")
        return choose_algorithm()
    
def solve_maze(algorithm, maze, start, goal):
    path = algorithm(maze, start, goal)
    if path:
        print ("Path Found! Path:", path)
        # visualise_maze(maze, path, start, goal)
    else:
        print("No path found!!")

def main():
    while True:
        algorithm = choose_algorithm()
        path = algorithm(maze, start, goal)
        if path:
            print ("Path Found! Path:", path)
            # visualise_maze(maze, path, start, goal)
        else:
            print("No path found!!")

if __name__ == "__main__":
    main()