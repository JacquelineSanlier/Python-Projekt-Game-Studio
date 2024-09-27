import pygame
import math

class Player:
    _x: int
    _y: int
    _speed: int
    def __init__(self, _x_init, _y_init, _speed_init):
        #initialize  the player with starting position and movementspeed
        self.rect = pygame.Rect(_x_init, _y_init, 50, 50) # square for the player (x, y, width, height)
        self.speed = _speed_init # movementspeed

    def move(self,keys):
        #moves the player based on the pressed key
        dx = 0
        dy = 0

        if keys['left']:
            dx = -self.speed
        if keys['right']:
            dx = self.speed
        if keys['up']:
            dy = -self.speed
        if keys['down']:
            dy = self.speed

        #  normlaize the movementspeed so if the player moves diagonal he wont get faster

        if dx != 0 and dy != 0:
            dx *= math.sqrt(0.5)
            dy *= math.sqrt(0.5)

        # refresh the player position

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        # draws the player as rectangle
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

class Controller:
    def __init__(self):
        # initialize the controller and safe the state of the keys
        self.keys = {
            'left' : False,
            'right' : False,
            'up' : False,
            'down' : False,
        }

    def handle_input(self):     
        # refresh the state of the key based on the pressed key
        pressed_keys = pygame.key.get_pressed()
        self.keys['left'] = pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]
        self.keys['right'] = pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]
        self.keys['up'] = pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]
        self.keys['down'] = pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]