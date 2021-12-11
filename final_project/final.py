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

# print formatted maze without commas
def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end = '')
        print()

# run program
maze = import_file("maze.txt")
maze = format_maze(maze)
start = start(maze)
print_maze(maze)
print('START: ', start)
