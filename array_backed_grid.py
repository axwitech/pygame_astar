"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
from node import Node
from map_generator import Map_generator

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
openlist = {}
closedlist = []
map_generator = Map_generator()

# a method that resets the nodes to their orignal state, this is called everytime the path is complete
# not the best solution, would be great to clear the both pathfinding lists and clear only the path


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
    # Set the specific nodes as red and not passable
    # grid[3][4].color = "red"
    # grid[4][4].color = "red"
    # grid[5][4].color = "red"
    # grid[6][4].color = "red"
    # grid[3][4].passable = False
    # grid[4][4].passable = False
    # grid[5][4].passable = False
    # grid[6][4].passable = False


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
# help method to help debug, prints out the neighbors of the clicked node


def print_out_neighbor(neighbor_list):
    for neighbor in neighbor_list:
        print(neighbor.name)

# method that calculates the h score
# https://en.wiktionary.org/wiki/Manhattan_distance


def calculate_h_score(start_x, start_y, end_x, end_y):
    x = abs(start_x - end_x)
    y = abs(start_y - end_y)
    answer = (x + y) * 10
    return answer


def clear_color_and_path(grid):
    for row in range(ROWS):
        for column in range(COLUMNS):
            grid[row][column].clear_node
            if grid[row][column].color == 'grey':
                grid[row][column].color = 'grey'
            elif grid[row][column].color == 'red':
                grid[row][column].color = 'red'
            else:
                grid[row][column].color = 'white'

# the main method that does the pathfinding


def find_path(start_x, start_y, end_x, end_y):
    # print("i am searching path from node", start_x, start_y, "to node", end_x, end_y)
    grid[start_x][start_y].color = "blue"
    grid[end_x][end_y].color = "blue"

    start_point = grid[start_x][start_y]
    end_point = grid[end_x][end_y]

    openlist[start_point] = 0

    while len(openlist) > 0:
        current = min(openlist, key=openlist.get)
        if current == end_point:
            openlist.clear()
            del closedlist[:]
            current.color = "yellow"
            path = []
            while current.parent:
                current.parent.color = "yellow"
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        closedlist.append(current)
        openlist.pop(current)
        for neighbor in current.neighbor:
            if neighbor in closedlist or neighbor.passable == False:
                # print("neighbor", neighbor.name, "is on closed list or is not passable")
                next
            else:
                # if the neighbor is not on the openlist, meaning that this is a completly new unvisited and unscored node then do this
                if (neighbor in openlist) == False:
                    # print("neighbor", neighbor.name, "is not on open list, adding it ")
                    # set the current node that we expecting  to the neighbors parent, so we can trace the path back if this is the optimal path
                    neighbor.parent = current
                    # set the gscore to the parents score + 10 if its a not a diagonal neighbor
                    neighbor.gscore = neighbor.parent.gscore + 10
                    # set the gscore to the parents score + 14 if its a diagonal neighbor
                    if neighbor.x != current.x and neighbor.y != current.y:
                        neighbor.gscore = neighbor.parent.gscore + 14
                    # calculate h score and set it
                    neighbor.hscore = calculate_h_score(
                        neighbor.x, neighbor.y, end_point.x, end_point.y)
                    # calculate f score and set it
                    neighbor.fscore = neighbor.hscore + neighbor.gscore
                    # add the neighbor to the openlist with the calculated f score
                    openlist[neighbor] = neighbor.fscore
                # if the neighbor is on the openlist we need to recalculate the fscore again
                elif neighbor in openlist:
                    # print("neighbor", neighbor.name, "is on the open list")
                    tempG = neighbor.parent.gscore + 10
                    neighbor.gscore = neighbor.parent.gscore + 10
                    if neighbor.x != current.x and neighbor.y != current.y:
                        neighbor.gscore = neighbor.parent.gscore + 14
                    if tempG < neighbor.gscore:
                        neighbor.gscore = tempG
                        neighbor.hscore = calculate_h_score(
                            neighbor.x, neighbor.y, end_point.x, end_point.y)
                        neighbor.fscore = neighbor.hscore + neighbor.gscore
                        openlist[neighbor] = neighbor.fscore


init_game()
map_generator.generate_map(grid)
# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(WIDTH + MARGIN) * ROWS, (HEIGHT + MARGIN) * COLUMNS]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

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
                clear_color_and_path(grid)
                # reset_colors()
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                start_x = row
                start_y = column
                # Set that location to one
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
                if grid[row][column].color == "red" and grid[row][column].color != 'grey':
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
                    find_path(start_x, start_y, end_x, end_y)

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
