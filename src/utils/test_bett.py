import pygame
import ui

main_entity=[]


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dclocktime = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

u = ui.screen_tile(pygame, screen, 1, None)
u._getX()
u.getY()
exit()

u=ui.screen_tile(pygame,screen,1,None)
u.setPosition(100,100)
u.setSize(50,75)
u.setHitbox(105,105,40,60)
main_entity.append(u)
u.getX()
print (main_entity[0].getX())
#main_entity = [{
#    ui:ui.screen_tile(pygame,screen,1,None),    
#}]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    
    # main_entity[0].update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()