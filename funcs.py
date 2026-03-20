def parse_input(filename):

    f = open(filename, 'r')
    lines = f.readlines() # creates list of strings
    start_position = tuple(int(x) for x in lines[1].strip().split('-')) # start position tuple
    teleports = {} # dictionary to hold teleport positions
    game_grid = [] # list to hold the grid representation
    for i in range(2, len(lines)):
        row = list(lines[i].strip()) 
        game_grid.append(row)
        for j, cell in enumerate(row):
            pos = (j, i - 2) # store the position as we iterate through
            if cell == 'X': # goal position tuple
                goal = pos  # j is x, i-2 is y (offset by 2 header lines)
            elif cell.isdigit():
                teleports[int(cell)] = pos

    f.close()

    return start_position, game_grid, goal, teleports

def get_cost(pos, grid):

    x, y = pos
    cell = grid[y][x]

    if cell == 'M':
        cost = 2
    elif cell == 'B':
        cost = 3
    else:
        cost = 1

    return cost

def heuristic(pos, goal, grid, teleports):
    x, y = pos
    x_goal, y_goal = goal
    cell = grid[y][x]
    if cell.isdigit() and int(cell)%2 == 1:
        exit_pos = teleports[int(cell) + 1]
        ex, ey = exit_pos
        return abs(x_goal - ex) + abs(y_goal - ey)

    return abs(x_goal - x) + abs(y_goal - y)

def get_neighbours(pos, grid, teleports):
    x, y = pos
    cell = grid[y][x]

    # special case: teleport entrance
    if cell.isdigit() and int(cell) % 2 == 1:
        return [teleports[int(cell) + 1]]
    
    neighbours = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:       # loop through x and y offsets in order (LEFT, RIGHT, UP, DOWN)
        nx, ny = x + dx, y + dy                             # apply offset to cell
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):  # check in bounds
            if grid[ny][nx] != 'W':                         # check if wall
                neighbours.append((nx, ny))                 # append if passes both checks

    return neighbours

def rebuild_path(search_path, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = search_path[current]

    path.reverse()
    return path

# def sum_cost(path, grid):
#     cost = 0
#     for cell in path:
#         cost += get_cost(cell, grid)

#     return cost
