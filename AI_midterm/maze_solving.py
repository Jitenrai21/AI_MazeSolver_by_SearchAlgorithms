
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

def input_maze():
    # print("Enter a maze where '0' represents open path and '1' represents walls.\n For example maze = [[1, 0, 1, 1, 1], [1,0,0,1,1]], is one example of maze with two 5-column rows.")
    # maze = []
    # rows = int(input("Enter number of rows for your maze: "))
    # for _ in range(rows):
    #     row = input()
    #     if set(row) >= {'0', '1'}:
    #         maze.append([int(c) for c in row])
    #     else:
    #         print("The input is invalid!! A row can only consist of 0's and 1's.")
    #         return input_maze()
    # return maze
    maze = []
    rows = int(input("Enter the number of rows for the maze: "))
    cols = int(input("Enter the number of columns for the maze: "))

    print("Enter the maze row by row. For example: 10010 for a 5-column row.")
    for _ in range(rows):
        row = input()
        if set(row) >= {'0', '1'}:
            maze.append([int(c) for c in row])
        else:
            print("The input is invalid!! A row can only consist of 0's and 1's.")
            return input_maze()
    
    def get_position(prompt):
        while True:
            pos = input(prompt)
            try:
                row, col = map(int, pos.split(','))
                if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0:
                    return (row, col)
                else:
                    print("Invalid!! The postion must be within the boundary and not a wall.")
            except ValueError:
                print("Invalid input format. Please enter the position as 'row,col' (e.g., '0,0').")
    start = get_position("Enter your start position in the maze: ")
    goal = get_position("Enter your goal position in the maze: ")

    return maze, start, goal

def predefined_maze():
    return [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1]
    ]

def solve_maze(algorithm, maze, start, goal):
    path = algorithm(maze, start, goal)
    if path:
        print ("Path Found! Path:", path)
        visualize_maze(maze, path, start, goal)
    else:
        print("No path found!!")
        
def visualize_maze(maze, path, start, goal):
    visual = [row[:] for row in maze]
    for (r,c) in path:
        if (r,c ) != start and (r,c) != goal:
            visual[r][c] = '•'
    visual[start[0]][start[1]] = 'S'
    visual[goal[0]][goal[1]] = 'G'

    for row in visual:
        print(' '.join(str(cell) for cell in row))

def main():
    while True:
        algorithm = choose_algorithm()

        choice = input("Do you want to create your own maze? (Y/N):")
        if choice.lower() == 'y':
            maze = input_maze()
        elif choice.lower() == 'n':
            maze = predefined_maze()
        else:
            print("Invalid input! Thus, the predefined maze is opted.")
            maze = predefined_maze

        solve_maze(algorithm, maze, start, goal)

        again = input("Do you want to solve another maze? (Y/N): ")
        if again.lower() != 'y':
             break
        
if __name__ == "__main__":
    main()