
#
# Images than are use in the game
# can be used on more places
# an enmy can look the same, a tree too
#
# we cann add movements,sequences  here or better in an other class where like:
# dieing, jumping, falling, landing, walking 
# 
# import os
# 1. Step:
# Load all Files in one array
# unique_entities=[
#    tiles.tile_item(pygame,1,"Tree",'./assets/svg/tree.svg'),
#    tiles.tile_item(pygame,2,"Road",'./assets/svg/road.svg'),
#    tiles.tile_item(pygame,3,"Hill",'./assets/svg/hill.svg')
# ]
#
# 2. Step Build up your Map
#   At the momenent there is no Class for the List, I wil create one
#   u=tiles.screen_tile(pygame,screen,5,tree,unique_entities[0])
#   u.setPosition(300,200)
#   u.setSize(200,200)
#   u.setHitbox(20,34,160,156)
#   main_entity.append(u)
#
# Late i will create a Json Array for entieies and you can get it by Name
# unique_entities=[
#    "tree":tiles.tile_item(pygame,1,"Tree",'./assets/svg/tree.svg'),
#    "road":tiles.tile_item(pygame,2,"Tree",'./assets/svg/road.svg'),
# ]
# and then have the Option
# level1=tile_list(pygame,screen)
# level1.add("tree",x,y,width,height,hit_x,hit_y,_hit_width,hit_height)
#   hitbox entries are not required
# or with 2 Parameters
# level1.add("tree",dictionary_item)
# or with
# level1.add("tree",full_dictionary)
#
# so it will be easy to create a map

import tiles

class tile_list:
    _pygame=None #Pygame 
    _item_list={}
    _max_id=0
    

    def __init__(self,pygame):
        self._pygame=pygame

    def add(self,name,src,width=None,height=None,hit_x=0,hit_y=0,hit_width=None,hit_height=None):
        self._max_id+=1   
        self._item_list[name]= tiles.tile_item(self._pygame,self._max_id,name,src)
        self._item_list[name].setSize(width,height)
        self._item_list[name].setHitbox(hit_x,hit_y,hit_width,hit_height)
        return

    def addItems(self,items):
        for item in items:
            #        name    src     x       y       Hit_x   Hit_y   Hit_w   Hit_h
            self.add(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
    
    def getItem(self,name):
        return self._item_list[name]
            


class tile_item:
    _id:int=0        # id 
    _src:str =""     # path
    _name:str =""    # name caan be found by Name  
    _image = None     # 

    _width:int = 0            #Width 
    _height:int = 0           #Height
    
    _hitbox_x:int = 0                #Collision Position relative to Image start X
    _hitbox_y:int = 0                #Collision Position relative to image start Y
    _hitbox_width:int = 0            #Collision Width 
    _hitbox_height:int = 0           #Collision Height
    
    #
    # Initialise and give 
    #
    def __init__(self,pygame,id,name,src):
        self._id    = id
        self._name  = name
        self._src   = src
        self._image = self.__load(pygame,src)

    

    def __load(self,pygame,src):
        #pygame.image.load(os.path.join('data', src))
        return pygame.image.load(src)

    def getImage(self):
        return self._image 
    
    def setHitbox(self,x=0,y=0,width=None,height=None):
        self._hitbox_x=x                #Collision Position relative to Image start X
        self._hitbox_y=y                #Collision Position relative to image start Y
        if (width !=None):
            self._hitbox_width=width
        else:
            self._hitbox_width=self._width
        if (height !=None):
            self._hitbox_height=height
        else:
            self._hitbox_height=self._height

    def setSize(self,width=None,height=None):
        w,h = self._image.get_size()
        if (width != None):
            self._width=width  
        else:
            self._width=w
        if (height !=None):
            self._height:height
        else:
            self._height=h

    


    



class screen_list:
    pass


# Tile = Item auf dem Bildschirm , Entity = Interagierendes Item
# you can resiz
# you can move

class screen_tile:  	
    _pygame = None            #Pygame
    _screen = None            #Screen whehre it is displayed
    _id:int = 0               #unique ID
    _interactive:bool = False #0 Not inteeractive 1 with collision
    _src: str = ""            #Image file
    _name:str = ""            #ZB "Baum"
    _x:int = 0                #Position X
    _y:int = 0                #Position Y
    _width:int = 0            #Width 
    _height:int = 0           #Height
    _scale:float = 1          #Scale Factor
    _tile=None                #has the src of the Image

	
	
    _dx:int =0				  #movement per 1/60s  -1 left +1 right 0 no move
    _dy:int =0                #movement per 1/60s  -1 up   +1 down  0 no move
    _speed:float =1           #Speed for the Movement (Steps to move or times)
    _hitbox_x:int = None                #Collision Position X
    _hitbox_y:int = None                #Collision Position Y
    _hitbox_width:int = None            #Collision Width 
    _hitbox_height:int = None           #Collision Height
    __TRANSPARENT = (0,0,0,0)        #Transparenter Hintergrund 0-255
    __BLUE        = (255,255,0)    #Transparenter Hintergrund 0-255
    __RED         = (255,0,0,128)    #Transparenter Hintergrund 0-255
	
	# Erstelle eine Surface mit Transparenz
	#transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
	#transparent_surface.fill(BLUE)  # Fülle die Surface mit transparenter Farbe
	# Zeichne die transparente Surface
    #screen.blit(transparent_surface, (rect_x, rect_y))
    

    def __init__(self,pygame,screen,id,tile=None):
        self._id=id
        self._tile=tile
        self._pygame=pygame
        self._screen=screen

    def setId(self,id):
        self._id=id

    def setName(self,name):
        self._name=name

    def setPosition(self,x,y):
        self._x=x
        self._y=y
        if (self._hitbox_x == None):
            self._hitbox_x=0
        if (self._hitbox_y == None):
            self._hitbox_y=0

    def setSize(self,width,height):
        self._width=width
        self._height=height
        if (self._hitbox_width == None):
            self._hitbox_width=width
        if (self._hitbox_height == None):
            self._hitbox_height=height

    def setHitbox(self,x,y,width,height):
        self._hitbox_x=x
        self._hitbox_y=y
        self._hitbox_width=width
        self._hitbox_height=height

    def setScale(self,scale):
        self._scale=scale

    def setMove(self,dx,dy):
        self._dx=dx*self._speed
        self._dy=dy*self._speed

    def setSpeed(self,speed=1):
        self._speed=speed
    
    def setTitle(self,tile):
        self._tile=tile

    def move(self,x,y):
	    #remove old from screen or show animation
        #move the tile
        self._x+=(self._dx * self._speed)
        self._y+=(self._dx * self._speed)        

    def remove():
        pass

    def hide():
        pass

    def collides():
        pass
    
    def _draw_rect(self):
        x=self._x * self._scale
        y=self._y * self._scale
        w=self._width * self._scale
        h=self._height * self._scale
        screen=self._screen
        # self._pygame.draw.rect(screen,self.__BLUE,(x,y,w,h),2)    
        self._pygame.draw.rect(screen,self.__BLUE,(x,y,w,h),2)

    def _draw_hitbox(self):
        x=(self._x+self._hitbox_x) * self._scale
        y=(self._y+self._hitbox_y) * self._scale
        w=self._hitbox_width * self._scale
        h=self._hitbox_height * self._scale
        screen=self._screen
        self._pygame.draw.rect(screen,self.__RED,(x,y,w,h),2)

    def _draw_image(self):
        x=self._x * self._scale
        y=self._y * self._scale
        w=self._width
        h=self._height
        if (self._tile._image == None):
            return
        
        image=self._tile._image
        image=self._pygame.transform.scale(image, (w, h))
        #rotated_image = pygame.transform.rotate(image, 45)
        screen=self._screen
        screen.blit(image, (x, y)) 



    def update(self):
        #print("Update")
        self._draw_image()
        self._draw_rect()
        self._draw_hitbox()

    def getX(self):
        return self._x

		

	
