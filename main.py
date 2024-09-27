import pygame
#from objs import creature                     # This imports the player and item modules from the src.objs package.
#from src.objs import item                       # This imports the player and item modules from the src.objs package.
#from src.utils import damage_calc               # This imports the damage_calc module from the src.utils package
from src.utils.player_controller import Player, Controller         # This imports the player_controller module from src.utils package 

pygame.init()


width = 1280            #Game window height and width
height = 720

display = pygame.display.set_mode((width, height))
pygame.display.flip()

# fps and clock generator
clock = pygame.time.Clock()
FPS = 60

# color
WHITE =(255, 255, 255)

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

    # refresh screen
    pygame.display.flip()

    # controll framerate
    clock.tick(FPS)
    
pygame.quit()

if __name__ == "__main__":                      # This line ensures that the code block is only executed if the script is run directly, not if it is imported as a module in another script.
    basE_item_test = item.Weapon(1,1,"Test",[0])  # This creates an instance of the ItemBase class from the item module with the parameters 1, 1, "Test".
    print (basE_item_test)                      # This prints the string representation of the basE_item_test object.
