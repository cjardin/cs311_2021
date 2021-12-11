import queue

# import txt file that contains maze
def import_file(file_name):
    file = open(file_name)
    maze = file.read()
    file.close()
    return maze

# format txt maze
def format_maze(maze):
    formatted_maze = []
    rows = maze.splitlines()

    for row in rows:
        formatted_maze.append(list(row))
    return formatted_maze

# locate start of maze
def start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'o':
                return row, col

# locate end of maze
def end(maze, moves):
    for x, position in enumerate(maze[0]):
        if position == 'o':
            start = i
            x = start
            y = 0
            for move in moves:
                if move == 'LEFT':
                    x -= 1
                elif move == 'RIGHT':
                    x += 1
                elif move == 'UP':
                    y -= 1
                elif move == 'DOWN':
                    y += 1

            if maze[y][x] == 'x':
                print('Solution :', moves)
                move(maze, moves)
                return True
            return False

# print formatted maze without commas
def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end = '')
        print()

# validate cells
def validate_cells(maze, moves):
    for i, position in enumerate(maze[0]):
        if position == 'o':
            start = i
            x = start
            y = 0
            for move in moves:
                if move == 'LEFT':
                    x -= 1
                elif move == 'RIGHT':
                    x += 1
                elif move == 'UP':
                    y -= 1
                elif move == 'DOWN':
                    y += 1

                if not (0 <= x < len(maze[0]) and 0 <= y < len(maze)):
                    return False
                elif (maze[y][x] == '#'):
                    return False

            return True


# assign move values
def move(maze, solution):
    x = start
    y = 0
    position = set()
    for move in solution:
        if move == 'LEFT':
            x -= 1
        elif move == 'RIGHT':
            x += 1
        elif move == 'UP':
            y -= 1
        elif move == 'DOWN':
            y += 1
        position.add((y, x))

    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if(y, x) in position:
                print('+ ', end = '')
            else:
                print(col + ' ' , end = '')
        print()

# run program
maze = import_file("maze.txt")
maze = format_maze(maze)
solution = ''
start = start(maze)
print_maze(maze)
print('START: ', start)

moves = queue.Queue()
moves.put('')

while not end(maze, solution):
    solution = moves.get() #dequeue
    for move in ['LEFT', 'RIGHT', 'UP', 'DOWN']:
        coordinate = solution + move
        if validate_cells(maze, coordinate):
            moves.put(coordinate)
