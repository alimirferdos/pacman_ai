from pacman_ai.layout import Layout
from pacman_ai.Sprites import *
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)


def load_layout():
    f = open("layout.txt")
    return Layout([line.strip() for line in f])


def setup_room_one(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()

    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [[0, 0, 6, 600],
             [0, 0, 600, 6],
             [0, 600, 606, 6],
             [600, 0, 6, 606],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # return our new list
    return wall_list


class Game:
    def __init__(self):
        # Call this function so the Pygame library can initialize itself
        pygame.init()

        # Create an 606x606 sized screen
        self.screen = pygame.display.set_mode([606, 606])

        # This is a list of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'RenderPlain.'
        # Set the title of the window
        pygame.display.set_caption('Pacman')

        # Create a surface we can draw on
        self.background = pygame.Surface(self.screen.get_size()).convert()

        # Fill the screen with a black background
        self.background.fill(black)

        self.clock = pygame.time.Clock()

        self.all_sprites_list = pygame.sprite.RenderPlain()

        self.block_list = pygame.sprite.RenderPlain()

        self.pacman_collide = pygame.sprite.RenderPlain()

        self.wall_list = setup_room_one(self.all_sprites_list)

    def start_game(self):

        # default locations for pacman
        w = 303 - 16  # Width
        p_h = (7 * 60) + 19  # pacman height
        # Create the player paddle object
        pacman = Player(w, p_h, "images/Trollman.png")
        self.all_sprites_list.add(pacman)
        self.pacman_collide.add(pacman)

        self.draw_grid()
        score = 0
        done = False

        while done is False:
            # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                pacman.move(event)

            # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

            # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
            pacman.update(self.wall_list)

            # See if the pacman block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(pacman, self.block_list, True)

            # Check the list of collisions.
            if len(blocks_hit_list) > 0:
                score += len(blocks_hit_list)

            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.screen.fill(black)

            self.wall_list.draw(self.screen)
            self.all_sprites_list.draw(self.screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            pygame.display.flip()

            self.clock.tick(10)

    def draw_grid(self):
        for row in range(19):
            for column in range(19):
                if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                    continue
                else:
                    block = Block(yellow, 4, 4)

                    # Set a random location for the block
                    block.rect.x = (30 * column + 6) + 26
                    block.rect.y = (30 * row + 6) + 26

                    b_collide = pygame.sprite.spritecollide(block, self.wall_list, False)
                    p_collide = pygame.sprite.spritecollide(block, self.pacman_collide, False)
                    if b_collide:
                        continue
                    elif p_collide:
                        continue
                    else:
                        # Add the block to the list of objects
                        self.block_list.add(block)
                        self.all_sprites_list.add(block)
