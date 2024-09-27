import pygame
import tiles as tiles

main_entity=[]
unique_entities=[]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dclocktime = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#t=tiles.tile_item(pygame,1,"Tree",'./assets/svg/tree.svg')
#unique_entries=tile_list.getImage()
t=tiles.tile_item(pygame,1,"Tree",'./assets/svg/tree.svg')
unique_entities.append(t)

i=unique_entities[0].getImage()

tree=unique_entities[0]

u=tiles.screen_tile(pygame,screen,1,unique_entities[0])
u.setPosition(100,100)
u.setSize(50,75)
#u.setHitbox(105,105,40,60)
main_entity.append(u)



u=tiles.screen_tile(pygame,screen,2,tree)
u.setPosition(200,100)
u.setSize(100,20)
#u.setHitbox(105,105,40,60)
main_entity.append(u)

u=tiles.screen_tile(pygame,screen,3,tree)
u.setPosition(300,150)
u.setSize(20,20)
#u.setHitbox(105,105,40,60)
main_entity.append(u)

u=tiles.screen_tile(pygame,screen,4,tree)
u.setPosition(100,170)
u.setSize(20,200)
#u.setHitbox(105,105,40,60)
main_entity.append(u)

u=tiles.screen_tile(pygame,screen,5,tree)
u.setPosition(300,200)
u.setSize(200,200)
u.setHitbox(20,34,160,156)
main_entity.append(u)


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
    screen.fill("black")

    #screen.blit(unique_entities[0].getImage(), (100, 150)) 
    #u._draw_image() 
    
    #screen.blit(t.getImage(), (200, 150)) 

    # pygame.draw.circle(screen, "red", player_pos, 40)

    for entity in main_entity:
        entity.update()

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