import random
ROWS = 30
COLUMNS = 30
WALLS = 40
ITERATIONS = 10


class Map_generator:
    def generate_map(self, grid):
        # randomly set a percentage of the tiles to be walls
        for row in range(ROWS):
            for column in range(COLUMNS):
                chance = random.randint(0, 100)
                current = grid[row][column]
                if chance <= WALLS:
                    for node in current.neighbor:
                        if node.x != current.x and node.y != current.y:
                            node.color = "white"
                            current.passable = True
                        else:
                            current.color = 'grey'
                            current.passable = False
        # set all the borders to walls, make them grey and make them not passable and mark the borders are border
        for row in range(COLUMNS):
            grid[0][row].passable = False
            grid[row][0].passable = False
            grid[COLUMNS - 1][row].passable = False
            grid[row][COLUMNS - 1].passaale = False
            grid[row][0].color = "grey"
            grid[0][row].color = "grey"
            grid[COLUMNS - 1][row].color = "grey"
            grid[row][COLUMNS - 1].color = "grey"
            grid[0][row].border = True
            grid[row][0].border = True
            grid[COLUMNS - 1][row].border = True
            grid[row][COLUMNS - 1].border = True

        for iteration in range(ITERATIONS):
            for row in range(ROWS):
                for column in range(COLUMNS):
                    if grid[row][column].border == False:
                        grey_color_count = 0
                        for node in grid[row][column].neighbor:
                            if node.color == 'grey':
                                grey_color_count = grey_color_count + 1
                        if grey_color_count >= 5:
                            grid[row][column].color = 'grey'
                            grid[row][column].passable = False
                        elif grey_color_count == 2:
                            grid[row][column].color = 'grey'
                            grid[row][column].passable = False
                        else:
                            grid[row][column].color = 'white'
                            grid[row][column].passable = True
        #Iteration that tries to remove diagonal walls
        
        for iteration in range(ITERATIONS):
            for row in range(ROWS):
                for column in range(COLUMNS):
                    if grid[row][column].border == False:
                        grey_color_count = 0
                        for node in grid[row][column].neighbor:
                            if node.color == 'grey':
                                grey_color_count = grey_color_count + 1
                        if grey_color_count >= 5:
                            grid[row][column].color = 'grey'
                            grid[row][column].passable = False
