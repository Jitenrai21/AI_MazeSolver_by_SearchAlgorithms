import heapq
from collections import deque

#depth-First Search
def dfs(maze, start, goal):
    stack = [start] # This initialize the stack with the start position
    visited = set()
    parent = {}

    while stack:
        current = stack.pop() # pops the values for row and column from the stack
        row, col = current

        if current == goal:
            path = []
            while current != start: # trace back the path from goal to start
                path.append(current)
                current = parent[current]
                #parent = {(3, 2): (2, 2), (2, 2): (1, 2), (1, 2): (1, 1), (1, 1): (0, 1), (0, 1): (0, 0)}
            path.append(start)
            path.reverse() # reverses the traced back path
            return path

        if current not in visited:
            visited.add(current)

            #explores all four possible neighbpring directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    neighbor = (new_row, new_col)
                    if neighbor not in visited:
                        parent[neighbor] = current
                        stack.append(neighbor)

    return None  # return None if no path is found

#Breadth-First Search
def bfs(maze, start, goal):
    queue = deque([(start, [start])]) # initialize queue with start and initial path
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

#Uniform Cost Search
def ucs(maze, start, goal):
    pq = [(0, start, [start])] #here, cost = 0, (row,col) = start, path= [start]
    visited = set()

    while pq:
        cost, (row, col), path = heapq.heappop(pq)

        if (row, col) == goal:
            return path
        
        if(row, col) not in visited:
            visited.add((row, col))

            directions = [(-1,0), (1,0), (0,-1), (0,1)] # possible movements

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # check neighbor for within boundary and open space
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    new_cost = cost + 1
                    heapq.heappush(pq, (new_cost, (new_row, new_col), path + [(new_row, new_col)]))
    return None

#helper function 
def manhattan_distance (point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) #gives absolute value with no negative value

#A* Search
def a_star(maze, start, goal):
    pq = [(manhattan_distance(start, goal), 0, start, [start])]
    visited = set()

    while pq:
        f, cost, (row, col), path = heapq.heappop(pq) # f = heuristics + cost

        if (row, col) == goal:
            return path
        
        if (row, col) not in visited:
            visited.add((row, col))
        
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    new_cost = cost + 1
                    h = manhattan_distance((new_row, new_col), goal) # heuristics calculation
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

#Function to choose a search algorithm
def choose_algorithm():
    print("Select a search algorithm:")
    print("1. Depth First Search (DFS)")
    print("2. Breadth First Search (BFS)")
    print("3. Uniform Cost Search (UCS)")
    print("4. A* Search")
    print("5. Best-First Search")

    choice = input("Enter the number for your chosen algorithm: ")

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

#Function to input a custom maze
def input_maze():
    maze = []
    rows = int(input("Enter the number of rows for the maze: "))
    cols = int(input("Enter the number of columns for the maze: "))

    print("Enter the maze row by row. For example: 10010 for a 5-column row.")
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ")
            if len(row) != cols:
                print(f"Invalid input!! The row can only have {cols} number of input for the maze.")
            elif set(row) <= {'0', '1'}:
                maze.append([int(c) for c in row]) #converts input string into a list of integers for the maze
                break
            else:
                print("Invalid input! The maze can only consist of '1' and '0' digits.")
    
    #function to get start and goal position
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

# Function to provide a predefined maze and positions
def predefined_maze():
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1]
    ]
    start = (0,1)
    goal = (4,3)
    return maze, start, goal

#Function to solve maze and give output
def solve_maze(algorithm, maze, start, goal):
    path = algorithm(maze, start, goal)
    if path:
        print ("Path Found! Path:", path)
        visualize_maze(maze, path, start, goal)
    else:
        print("No path found! Try by different or opt to some other maze.")

#Function to display visualization of initial maze
def visualize_initial_maze(maze):
    print("Initial maze layout:")
    for row in maze:
        print(" ".join(str(cell) for cell in row))


#Function to display visualization of maze with path       
def visualize_maze(maze, path, start, goal):
    visual = [row[:] for row in maze] #creates a copy of the maze for visualization
    for (r,c) in path:
        if (r,c ) != start and (r,c) != goal:
            visual[r][c] = '•' #this marks the path
    visual[start[0]][start[1]] = 'S' #Start position in maze
    visual[goal[0]][goal[1]] = 'G'  #goal position in maze

    for row in visual:
        print(' '.join(str(cell) for cell in row))#printing visualized maze

#Main function to run the maze solver program
def main():
    while True:
        algorithm = choose_algorithm()

        choice = input("Do you want to create your own maze? (Y/N):")
        if choice.lower() == 'y':
            maze, start, goal = input_maze()
        elif choice.lower() == 'n':
            maze, start, goal = predefined_maze()
        else:
            print("Invalid input! Thus, the predefined maze is opted.")
            maze, start, goal = predefined_maze()

        visualize_initial_maze(maze)

        solve_maze(algorithm, maze, start, goal)

        again = input("Do you want to solve another maze? (Y/N): ")
        if again.lower() != 'y':
             break #ends loop if the user prompts to not to solve another maze.
    print("Hence, This was the maze solver project of Jiten Rai. Thank you!!")
        
if __name__ == "__main__":
    main()