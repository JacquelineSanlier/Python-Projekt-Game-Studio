import pygame
#from objs import creature                     # This imports the player and item modules from the src.objs package.
#from src.objs import item                       # This imports the player and item modules from the src.objs package.
#from src.utils import damage_calc               # This imports the damage_calc module from the src.utils package
from src.utils.player_controller import Player, Controller         # This imports the player_controller module from src.utils package 
from src.utils.ui import WindowBase, TextBase

pygame.init()


width = 1280            #Game window height and width
height = 720

display = pygame.display.set_mode((width, height))
pygame.display.flip()

#test ui window
window = WindowBase(1, display, 100, 10, int(width/2), int(height*0.05), True)
window2 = WindowBase(1, display, 100, 10, int(width/2), int(height*0.95), True)
texttest = TextBase(1,"Hallo Welt", display, 20, int(height*0.95), 3)
window._color = "black"
window2._color = "black"

# fps and clock generator
clock = pygame.time.Clock()
FPS = 60

# color
WHITE = (255, 255, 255)

# create player and controller
player = Player(400, 300, 5) # player object with start position and speed
controller = Controller() #controller for input

is_running = True       #This keeps the game window open
while is_running:
    for event in pygame.event.get():        #Quit game with x button
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    
    # get input
    controller.handle_input()

    # move the player
    player.move(controller.keys)
 
    # fill the screen and move player
    display.fill(WHITE)
    player.draw(display)

    #render ui after player logic always
    window.update()
    window2.update()
    texttest.update()

    # refresh screen
    pygame.display.flip()

    # controll framerate
    clock.tick(FPS)
    
pygame.quit()
