class Layout:
    """
  A Layout manages the static information about the game board.
  """

    def __init__(self, layout_text):
        self.width = len(layout_text[0])
        self.height = len(layout_text)
        self.walls = [[False for y in range(self.height)] for x in range(self.width)]
        self.food = [0, 0]
        self.agentPositions = (0, 0)
        self.process_layout_text(layout_text)

    def is_wall(self, pos):
        x, col = pos
        return self.walls[x][col]

    def process_layout_text(self, layout_text):
        for y in range(self.height):
            for x in range(self.width):
                layoutChar = layout_text[y][x]
                self.process_layout_char(x, y, layoutChar)

    def process_layout_char(self, x, y, layoutChar):
        if layoutChar == '%':
            self.walls[x][y] = True
        elif layoutChar == '.':
            self.food[0] = x
            self.food[1] = y
        elif layoutChar == 'P':
            self.agentPositions = (x, y)

    def get_walls(self):
        walls = []
        for x in range(self.width):
            for y in range(self.height):
                if self.walls[x][y] is True:
                    walls.append((x, y))
        return walls

