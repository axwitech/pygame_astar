import random
ROWS = 30
COLUMNS = 30
WALLS = 40
ITERATIONS = 5


class Map_generator:
    def generate_map(self, grid):
        # randomly set a percentage of the tiles to be walls
        for row in range(ROWS):
            for column in range(COLUMNS):
                # grid[row][column].color = random.choice(['grey', 'white']
                chance = random.randint(0, 100)
                if chance <= WALLS:
                    grid[row][column].color = 'grey'
                    grid[row][column].passable = False
        # set all the borders to walls
        for row in range(COLUMNS):
            grid[0][row].passable = False
            grid[row][0].passable = False
            grid[COLUMNS - 1][row].passable = False
            grid[row][COLUMNS - 1].passaale = False
            grid[row][0].color = "grey"
            grid[0][row].color = "grey"
            grid[COLUMNS - 1][row].color = "grey"
            grid[row][COLUMNS - 1].color = "grey"
        # a. iterate over each cell.
        # b. if a 3x3 grid centered over the cell contains at least five walls, it stays a wall.
        # c. otherwise, it becomes/stays empty.
        for iteration in range(ITERATIONS):
            for row in range(ROWS):
                for column in range(COLUMNS):
                    grey_color_count = 0
                    for node in grid[row][column].neighbor:
                        if node.color == 'grey':
                            grey_color_count = grey_color_count + 1
                            # print(grey_color_count)
                    if grey_color_count > 5:
                        grid[row][column].color = 'grey'
