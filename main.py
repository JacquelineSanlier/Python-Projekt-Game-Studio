import pygame
from src.objs.creature import CreatureBase                    # This imports the player and item modules from the src.objs package.
#from src.objs import item                       # This imports the player and item modules from the src.objs package.
from src.utils.damage_calc import calculate_damage               # This imports the damage_calc module from the src.utils package
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

# placeholder Creatures to have something to calculate
creature_1 = CreatureBase(1, 'Goblin', 30, 3, 50)
creature_2 = CreatureBase(1, 'Orc', 50, 5, 50)

text_surface = None     # Combat Text placeholder
start_time = None       # tracking time elapsed (for drawing combat text over x frames)

# create player and controller
player = Player(400, 300, 5) # player object with start position and speed
controller = Controller() #controller for input

is_running = True       #This keeps the game window open
while is_running:

    current_time = pygame.time.get_ticks()      # get time at the start of the loop (for combat text initialization)

    for event in pygame.event.get():        #Quit game with x button
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            if event.key == pygame.K_e:                                              # run combat text once e is pressed / test
                text_surface, start_time = calculate_damage(creature_1, creature_2)   # creatures are currently dummies

    
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

    # combat text screen
    if text_surface and start_time and current_time - start_time < 1000:
        display.blit(text_surface, ((width // 2) - 100, (height // 2) + 200))

    # refresh screen
    pygame.display.flip()

    # controll framerate
    clock.tick(FPS)
    
pygame.quit()
