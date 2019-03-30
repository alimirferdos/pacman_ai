import pygame
from pacman_ai.Globals import *


class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    # This class represents the bar at the bottom that the player controls


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.image.load(filename).convert()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.change_x = 0
        self.change_y = 0
        self.move_one_bool = False

    # Change the speed of the player
    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Find a new position for the player
    def update(self, walls):
        # Get the old position, in case we need to go back to it
        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y

        if self.move_one_bool:
            self.move_one_bool = False
            self.change_speed(-self.change_x, -self.change_y)

            # Did this update cause us to hit a wall?
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left = old_x
        else:

            self.rect.top = new_y

            # Did this update cause us to hit a wall?
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                # Whoops, hit a wall. Go back to the old position
                self.rect.top = old_y

    def move(self, direction):
        if direction == Directions.WEST:
            self.change_speed(-AGENT_MOVE, 0)
            self.move_one_bool = True
        if direction == Directions.EAST:
            self.change_speed(AGENT_MOVE, 0)
            self.move_one_bool = True
        if direction == Directions.NORTH:
            self.change_speed(0, -AGENT_MOVE)
            self.move_one_bool = True
        if direction == Directions.SOUTH:
            self.change_speed(0, AGENT_MOVE)
            self.move_one_bool = True

    def move_keyboard(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.change_speed(-AGENT_MOVE, 0)
                self.move_one_bool = True
            if event.key == pygame.K_RIGHT:
                self.change_speed(AGENT_MOVE, 0)
                self.move_one_bool = True
            if event.key == pygame.K_UP:
                self.change_speed(0, -AGENT_MOVE)
                self.move_one_bool = True
            if event.key == pygame.K_DOWN:
                self.change_speed(0, AGENT_MOVE)
                self.move_one_bool = True

