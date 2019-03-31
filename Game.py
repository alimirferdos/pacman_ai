from pacman_ai.layout import load_layout
from pacman_ai.Sprites import *
from pacman_ai.Search import dfs, bfs, ucs


def setup_room_one(all_sprites_list, layout):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()
    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [[x * TILE_POSITIONING, y * TILE_POSITIONING, TILE_SIZE, TILE_SIZE] for x, y in layout.get_walls()]

    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # return our new list
    return wall_list


class Game:
    def __init__(self):
        self.layout = load_layout()
        # Call this function so the Pygame library can initialize itself
        pygame.init()

        # Create a screen
        self.screen = pygame.display.set_mode([self.layout.height * TILE_POSITIONING,
                                               self.layout.width * TILE_POSITIONING])

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

        self.wall_list = setup_room_one(self.all_sprites_list, self.layout)

    def start_game(self):
        # Create the player paddle object
        pacman_position = self.layout.agentPositions
        pacman = Player(pacman_position[1] * TILE_POSITIONING, pacman_position[0] * TILE_POSITIONING,
                        "images/Trollman.png")
        self.all_sprites_list.add(pacman)
        self.pacman_collide.add(pacman)

        # self.draw_grid()
        goal_pass = ucs(self.layout)
        self.move_pacman(pacman, goal_pass)

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

    def move_pacman(self, pacman, goal_pass):
        for m in goal_pass:
            # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
            # for event in pygame.event.get():
            #     pacman.move_keyboard(event)
            # print(m)
            pacman.move(m)

            # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
            pacman.update(self.wall_list)

            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.screen.fill(black)

            self.wall_list.draw(self.screen)
            self.all_sprites_list.draw(self.screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            pygame.display.flip()

            self.clock.tick(20)
