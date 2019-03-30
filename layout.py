class Layout:
    """
  A Layout manages the static information about the game board.
  """

    def __init__(self, layout_text):
        self.width = len(layout_text[0])
        self.height = len(layout_text)
        self.walls = [[0 for y in range(self.height)] for x in range(self.width)]
        self.food = [0, 0]
        self.agentPositions = []
        self.process_layout_text(layout_text)

    def is_wall(self, pos):
        x, col = pos
        return self.walls[x][col]

    def process_layout_text(self, layout_text):
        maxY = self.height - 1
        for y in range(self.height):
            for x in range(self.width):
                layoutChar = layout_text[maxY - y][x]
                self.process_layout_char(x, y, layoutChar)
        self.agentPositions.sort()
        self.agentPositions = [(i == 0, pos) for i, pos in self.agentPositions]

    def process_layout_char(self, x, y, layoutChar):
        if layoutChar == '%':
            self.walls[x][y] = True
        elif layoutChar == '.':
            self.food[0] = x
            self.food[1] = y
        elif layoutChar == 'P':
            self.agentPositions.append((0, (x, y)))
