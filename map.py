import pygame
from node import Node
from map_generator import Map_generator
from pathfinder import Pathfinder

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# HOW MANY NODES WE WANT
ROWS = 30
COLUMNS = 30

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
map_generator = Map_generator()
pathfinder = Pathfinder()
# method that initiates the grid and initiates the map. updates the neighbors for it too.


def init_game():
    del grid[:]
    for row in range(ROWS):
        # Add an empty array that will hold each node
        # in this row
        grid.append([])
        for column in range(COLUMNS):
            node = Node()
            node.x = row
            node.y = column
            node.color = "white"
            node.name = "My name is: ", node.x, node.y
            grid[row].append(node)  # Append a cell
    update_neighbors()

# method that updates the nodes with the information of their neighbors


def update_neighbors():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if row > 0:
                grid[row][column].neighbor = grid[row - 1][column]
            if row < ROWS - 1:
                grid[row][column].neighbor = grid[row + 1][column]
            if column > 0:
                grid[row][column].neighbor = grid[row][column - 1]
            if column < COLUMNS - 1:
                grid[row][column].neighbor = grid[row][column + 1]
            if row > 0 and column > 0:
                grid[row][column].neighbor = grid[row - 1][column - 1]
            if row > 0 and column < COLUMNS - 1:
                grid[row][column].neighbor = grid[row - 1][column + 1]
            if row < ROWS - 1 and column > 0:
                grid[row][column].neighbor = grid[row + 1][column - 1]
            if row < ROWS - 1 and column < COLUMNS - 1:
                grid[row][column].neighbor = grid[row + 1][column + 1]


init_game()
map_generator.generate_map(grid)
# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [((WIDTH + MARGIN) * ROWS) + MARGIN, ((HEIGHT + MARGIN) * COLUMNS) + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Pathfinding and Random levels")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pathfinder.clear_color_and_path(grid)
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                start_x = row
                start_y = column
                if grid[row][column].color == "red":
                    # print("Grid coordinates: ", row, column, "Node color: ", grid[row][column].color, "Node is passable: ", grid[row][column].passable,
                    #      "Node name is: ", grid[row][column].name, "My neighbors are :", "My neighbors are: ", print_out_neighbor(grid[row][column].neighbor))
                    next
                elif grid[row][column].color != 'grey':
                    grid[row][column].color = "green"
                    # print("Grid coordinates: ", row, column, "Node color: ", grid[row][column].color, "Node is passable: ", grid[row][column].passable,
                    #      "Node name is: ", grid[row][column].name, "My neighbors are :", "My neighbors are: ", print_out_neighbor(grid[row][column].neighbor))
            elif event.button == 2:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if grid[row][column].color == "red":
                    grid[row][column].color == "white"
                    # print("Grid coordinates: ", row, column, "Node color: ", grid[row][column].color, "Node is passable: ",grid[row][column].passable, "Node name is: ", grid[row][column].name, "My neighbors are :" , "My neighbors are: ", print_out_neighbor(grid[row][column].neighbor))
                elif grid[row][column].color != 'grey':
                    grid[row][column].color = "red"
                    grid[row][column].passable = False
                    # print("Grid coordinates: ", row, column, "Node color: ", grid[row][column].color, "Node is passable: ",grid[row][column].passable, "Node name is: ", grid[row][column].name, "My neighbors are :" , "My neighbors are: ", print_out_neighbor(grid[row][column].neighbor))

            elif event.button == 3:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                end_x = row
                end_y = column
                # Set that location to one
                if grid[row][column].color == "red":
                    # print("Grid coordinates: ", row, column, "Node color: ", grid[row][column].color, "Node is passable: ", grid[row][column].passable,
                    #      "Node name is: ", grid[row][column].name, "My neighbors are :", "My neighbors are: ", print_out_neighbor(grid[row][column].neighbor))
                    next
                elif grid[row][column].color != 'grey':
                    grid[row][column].color = "green"
                    # print("Grid coordinates: ", row, column, "Node color: ", grid[row][column].color, "Node is passable: ", grid[row][column].passable,
                    #      "Node name is: ", grid[row][column].name, "My neighbors are :", "My neighbors are: ", print_out_neighbor(grid[row][column].neighbor))
                    pathfinder.find_path(grid, start_x, start_y, end_x, end_y)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = WHITE
            if grid[row][column].color == "green":
                color = GREEN
            elif grid[row][column].color == "red":
                color = RED
            elif grid[row][column].color == "blue":
                color = BLUE
            elif grid[row][column].color == "yellow":
                color = YELLOW
            elif grid[row][column].color == "white":
                color = WHITE
            elif grid[row][column].color == "grey":
                color = GREY
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
