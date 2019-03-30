from pacman_ai.Globals import Directions


class Layout:
    """
  A Layout manages the static information about the game board.
  """

    def __init__(self, layout_text):
        self.width = len(layout_text)
        self.height = len(layout_text[0])
        self.walls = [[False for y in range(self.width)] for x in range(self.height)]
        self.food = [0, 0]
        self.agentPositions = (0, 0)
        self.process_layout_text(layout_text)

    def is_wall(self, pos):
        x, col = pos
        return self.walls[col][x]

    def is_goal(self, pos):
        return self.food[0] == pos[0] and self.food[1] == pos[1]

    def process_layout_text(self, layout_text):
        for x in range(self.height):
            for y in range(self.width):
                layoutChar = layout_text[y][x]
                self.process_layout_char(x, y, layoutChar)

    def process_layout_char(self, x, y, layout_char):
        if layout_char == '%':
            self.walls[x][y] = True
        elif layout_char == '.':
            self.food[0] = y
            self.food[1] = x
        elif layout_char == 'P':
            self.agentPositions = (y, x)

    def get_walls(self):
        walls = []
        for x in range(self.height):
            for y in range(self.width):
                if self.walls[x][y] is True:
                    walls.append((x, y))
        return walls

    def get_neighbours(self, pos):
        x = pos[0]
        y = pos[1]
        neighbours = []

        if y != self.height - 1 and not self.is_wall((x, y + 1)):
            neighbours.append(((x, y + 1), "East"))
        if x != self.width - 1 and not self.is_wall((x + 1, y)):
            neighbours.append(((x + 1, y), "South"))
        if x != 0 and not self.is_wall((x - 1, y)):
            neighbours.append(((x - 1, y), "North"))
        if y != 0 and not self.is_wall((x, y - 1)):
            neighbours.append(((x, y - 1), "West"))
        return neighbours
