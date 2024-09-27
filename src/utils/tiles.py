
#
# Images than are use in the game
# can be used on more places
# an enmy can look the same, a tree too
#
# we cann add movements,sequences  here or better in an other class where like:
# dieing, jumping, falling, landing, walking 
# 
# import os

class tile_item:
    _id:int=0        # id 
    _src:str =""     # path
    _name:str =""    # name caan be found by Name  
    _image = None     # 

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
        # print(self._tile._name)
        # screen=self._screen
        #image=self._pygame.image.load('./assets/svg/tree.svg'); 
        #image=self._pygame.image.load('./assets/svg/tree.svg'); 


        # image=self._tile.getImage()
        x=self._x * self._scale
        y=self._y * self._scale
        w=self._width
        h=self._height
        image=self._tile._image
        image=self._pygame.transform.scale(image, (w, h))
        #pygame.transform.rotate()
        #rotated_image = pygame.transform.rotate(image, 45)
        screen=self._screen
        screen.blit(image, (x, y)) 



    def update(self):
        #print("Update")
        self._draw_image()
        self._draw_rect()
        self._draw_hitbox()


		

	
