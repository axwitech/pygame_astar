ROWS = 30
COLUMNS = 30
openlist = {}
closedlist = []
path = []


class Pathfinder:

    def calculate_h_score(self, start_x, start_y, end_x, end_y):
        x = abs(start_x - end_x)
        y = abs(start_y - end_y)
        answer = (x + y) * 10
        return answer

    def clear_color_and_path(self, grid):
        openlist.clear()
        del closedlist[:]
        del path[:]
        for row in range(ROWS):
            for column in range(COLUMNS):
                grid[row][column].clear_node
                if grid[row][column].color == 'grey':
                    grid[row][column].color = 'grey'
                    grid[row][column].passable = False
                elif grid[row][column].color == 'red':
                    grid[row][column].color = 'red'
                else:
                    grid[row][column].color = 'white'

    def find_path(self, grid, start_x, start_y, end_x, end_y):
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
                        neighbor.hscore = self.calculate_h_score(
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
                            neighbor.hscore = self.calculate_h_score(
                                neighbor.x, neighbor.y, end_point.x, end_point.y)
                            neighbor.fscore = neighbor.hscore + neighbor.gscore
                            openlist[neighbor] = neighbor.fscore
