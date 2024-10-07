
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
# level_tiles = [
#   ["Tree"  ,100,100],
#   ["Grass" ,100,200,64,64],
#   ["Grass" ,100,300,128,128]
# ]
#
# EXAMPLE
#
# Parameters of the array:
#   name    = not uniqe the name of the Item
#   filename= of the Image we use, if we use 
#   x       = x - position of the item
#   y       = y - position of the item
#   width   = x - optional new With   instead of the original 
#   height  = x - optional new height instead of the orioginal
#
# unique-tiles=[
#   ["Tree",'./assets/svg/tree.svg'  ,64,64, 5,12,52,52],
#   ["Road",'./assets/svg/road.svg'  ,64,64,17, 0,32,64],
#   ["Grass",'./assets/svg/grass.svg',64,64, 5,10,55,54]
# ]
#
# Parameters of the array:
#   name    = not uniqe the name of the Item
#   x       = x - position of the item
#   y       = y - position of the item
#   width   = x - optional new With   instead of the original 
#   height  = x - optional new height instead of the orioginal
#
# level_tiles = [
#   ["Tree"  ,100,100],
#   ["Grass" ,100,200,64,64],
#   ["Grass" ,100,300,128,128]
# ]
# pygame.init()
# pygamme_screen = pygame.display.set_mode((1280, 720))
# myscreen = screen(pygame,pygame_screen)
# myscreen.setTiles(unique_tiles)
# myscreen.addItems(level_tiles)

class tile_list:
    _pygame=None #Pygame 
    _item_list={}
    _max_id=0
    

    def __init__(self,pygame):
        self._pygame=pygame

    def add(self,name,src,width=None,height=None,hit_x=0,hit_y=0,hit_width=None,hit_height=None):
        self._max_id+=1   
        self._item_list[name]= tile_item(self._pygame,self._max_id,name,src)
        self._item_list[name].setSize(width,height)
        self._item_list[name].setHitbox(hit_x,hit_y,hit_width,hit_height)
        return

    def addItems(self,items):
        for item in items:
            #        name    src     width   height      Hit_x   Hit_y   Hit_w   Hit_h
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
            self._height=height
        else:
            self._height=h

class screen:
    _pygame=None    #Empty Python container
    _screen=None    #Screen entity
    _tile_list={}   #Used Items width changes sizes
    _clock=None     #Timer
    _item_list={}   #All unique Items in Original size 
    _id:int = 0     #unique ID
    _offset_x=50    #Posiiton of map_area
    _offset_y=100   #Position of Map area
    xd=0            #moving Direction x 
    yd=0            #movinf Direction y
    # scale:float=1   #Global user scale

    _player={}              #Used Player Items
    _player_item_id:int =0  #Numer of the Item the Player is displayed


    def __init__(self,pygame,screen):
        self._pygame  = pygame
        self._screen  = screen
    

    #Global Unique Entities/Tiles
    def setTiles(self,tiles):
        self._tile_list=tile_list(self._pygame)
        self._tile_list.addItems(tiles)
    
    #
    # PRIVATE
    # 
    # creates an item to append on screen or player
    #
    # SYNTAX
    #   myscreen.add("Tree",100,150,64,64)
    #   myscreen.add("Grass",300,250)
    #
    # Parameters:
    #   name    = not uniqe the name of the Item
    #   x       = x - position of the item
    #   y       = y - position of the item
    #   width   = x - optional new With   instead of the original 
    #   height  = x - optional new height instead of the orioginal
    #
    def _createItem(self,name,x,y,width=None,height=None,rotation=None):
        tile=self._tile_list.getItem(name)

        item=screen_tile(self,tile)
        #item=screen_tile(self._pygame, self._screen, self, self._id, tile)
        item.setPosition(x,y)

        if (width and height):
            item.setSize(width,height)

        if(rotation):
            item.setRotation(rotation)

        return item
    

    #
    # PUBLIC
    # 
    # appends a new Item to the screen
    #
    # SYNTAX
    #   myscreen.add("Tree",100,150,64,64)
    #   myscreen.add("Grass",300,250)
    #
    # Parameters:
    #   name    = not uniqe the name of the Item
    #   x       = x - position of the item
    #   y       = y - position of the item
    #   width   = x - optional new With   instead of the original 
    #   height  = x - optional new height instead of the orioginal
    #
    def add(self,name,x,y,width=None,height=None,rotation=None):
        self._id+=1
        self._item_list[self._id]=self._createItem(name,x,y,width,height,rotation)    
        return self._item_list[self._id]
    
    #
    # PUBLIC
    # 
    # SYNTAX
    #   myscreen.addItem(array)
    #
    # Parameters of the array:
    #   name    = not uniqe the name of the Item
    #   x       = x - position of the item
    #   y       = y - position of the item
    #   width   = x - optional new With   instead of the original 
    #   height  = x - optional new height instead of the orioginal
    #   rotation= Start Rotation
    #
    #   infollowing format:
    #   array = ["Tree" ,100,100]
    #   array = ["Tree" ,100,100,32,64]
    #
    def addItem(self,item):
        item.append(5-len(item))
        
        #for i in range (2,5):
        #    item[i]=0
        self.add(item[0],item[1],item[2],item[3],item[4],item[5])

    #
    # PUBLIC
    # 
    # SYNTAX
    #   myscreen.addItems(dictionary)
    #
    # Parameters of the array:
    #   name    = not uniqe the name of the Item
    #   x       = x - position of the item
    #   y       = y - position of the item
    #   width   = x - optional new With   instead of the original 
    #   height  = x - optional new height instead of the orioginal
    #   infollowing format:
    #   dictionary = [
    #       ["Tree" ,100,100],
    #       ["Road" ,100,200,64,64],
    #       ["Grass",100,300,128,128]
    #   ]
    #
    def addItems(self,items):
        for item in items:
            self.addItem(item)


    def addPlayer(self,items):
        for item in items:
            item.append(5-len(item))
            self._player_item_id+=1
            self._player[self._player_item_id]=self._createItem(item[0],item[1],item[2],item[3],item[4],item[5])


    #
    # PUBLIC
    # 
    # SYNTAX
    #   item=myscreen.getItem(index)
    #
    # PARAMETERS:
    #   index: the unique Number of the object
    # 
    # Returns
    #   item    = the Item-object of the list
    #
    def getItem(self,index):
        return self._item_list[index]
        

    # 
    # PUBLIC
    #
    # Updates the Graphic
    #
    # SYNTAX
    #   myscreen.update()
    #  
    def update(self):
        for item in self._item_list.values():
            self.move()
            item.update()

        for item in self._player.values():
            #self.move()
            item.update_player()


    def move(self):
        self._offset_x+=self.xd
        self._offset_y+=self.yd
    
    def setDev(self,dev=True):
        for item in self._item_list.values():
            item._dev=dev

    def toggleDev(self):
        for item in self._item_list.values():
            item._dev=not item._dev

    def setScale(self,scale):
        for item in self._item_list.values():
            item._scale=scale

    def adjustScale(self,scale):
        for item in self._item_list.values():
            item._scale=item._scale*scale



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
    _width:int = None         #Width 
    _height:int = None        #Height
    _scale:float = 1          #Scale Factor
    _startrotation:int = 0    #Rotation          
    _tile=None                #has the src of the Image
    _dev=False                #Develper Mode

    _dx:int =0				  #movement per 1/60s  -1 left +1 right 0 no move
    _dy:int =0                #movement per 1/60s  -1 up   +1 down  0 no move
    _speed:float =1           #Speed for the Movement (Steps to move or times)

    _hitbox_x:int = None                #Collision Position X
    _hitbox_y:int = None                #Collision Position Y
    _hitbox_width:int = None            #Collision Width 
    _hitbox_height:int = None           #Collision Height
    _original_width = None              #from tile or other
    _original_height = None             #from tile or other
    _original_hitbox_x:int = None       #Collision Position X
    _original_hitbox_y:int = None       #Collision Position Y
    _original_hitbox_width:int = None   #Collision Width 
    _original_hitbox_height:int = None  #Collision Height
    
    __TRANSPARENT = (0,0,0,0)           #Transparenter Hintergrund 0-255
    __BLUE        = (255,255,0)         #Transparenter Hintergrund 0-255
    __RED         = (255,0,0,128)       #Transparenter Hintergrund 0-255




	# Erstelle eine Surface mit Transparenz
	#transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
	#transparent_surface.fill(BLUE)  # Fülle die Surface mit transparenter Farbe
	# Zeichne die transparente Surface
    #screen.blit(transparent_surface, (rect_x, rect_y))
    
    #item=screen_tile(self._pygame, self._screen, self, self._id, tile)

    def __init__(self,parent,tile):
        #self._id=id
        #self._tile=tile
        #self._pygame=pygame
        #self._screen=screen

        self._parent=parent
        self._id=parent._id
        self._tile=tile
        self._pygame=parent._pygame
        self._screen=parent._screen

        if (tile):
            self.setSize(tile._width, tile._height)

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

    def _storeOriginalSize(self):
        if self._tile:
            if self._original_width == None:
                self._original_width=self._tile._width
            if self._original_height == None:
                self._original_height=self._tile._height
        if self._original_width == None:
            self._original_width=self._width
        if self._original_height == None:
            self._original_height=self._height

    def _storeOriginalHitbox(self):
        if self._tile:
            if self._original_hitbox_width == None:
                self._original_hitbox_width=self._tile._hitbox_width
            if self._original_hitbox_height == None:
                self._original_hitbox_height=self._tile._hitbox_height
            if self._original_hitbox_x == None:
                self._original_hitbox_x=self._tile._hitbox_x
            if self._original_hitbox_y == None:
                self._original_hitbox_y=self._tile._hitbox_y

        if self._original_hitbox_width == None:
            self._original_hitbox_width=self._hitbox_width
        if self._original_hitbox_height == None:
            self._original_hitbox_height=self._hitbox_height
        if self._original_hitbox_x == None:
            self._original_hitbox_x=self._tile._hitbox_x
        if self._original_hitbox_y == None:
            self._original_hitbox_y=self._tile._hitbox_y

    def setSize(self,width,height):
        #w=self._width
        #h=self._height

    
        self._width=width
        self._height=height

        self._storeOriginalSize()
        self.resizeHitbox(width,height)

    
    #resize Hitbox from w,h to width height
    # 2 Angaben nur die Neue
    def resizeHitbox(self,width,height):
        if (self._hitbox_width == None):
            self.setHitbox(self._x,self._y,self._width,self._height)
        if self._width == 0 or self._height == 0:
            return

        self._hitbox_width   =self._original_hitbox_width*width/self._width
        self._hitbox_height  =self._original_hitbox_height*height/self._height
        self._hitbox_x       =self._original_hitbox_x*width/self._width
        self._hitbox_y       =self._original_hitbox_y*height/self._height

    def setHitbox(self,x,y,width,height):
        self._hitbox_x=x
        self._hitbox_y=y
        self._hitbox_width=width
        self._hitbox_height=height
        self._storeOriginalHitbox()

    def setScale(self,scale):
        self._scale=scale

    def setMove(self,dx,dy):
        self._dx=dx*self._speed
        self._dy=dy*self._speed

    def setSpeed(self,speed=1):
        self._speed=speed
    
    def setTitle(self,tile):
        self._tile=tile

    def setRotation(self,r):
        self._startrotation=r

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


    def rotateRect(self,x,y,w,h,color,rot):
        pygame=self._pygame
        rect_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, color, (0, 0, w, h), 2)
        rotated_rect = pygame.transform.rotate(rect_surface, rot)
        rect = rotated_rect.get_rect(center=(x + w // 2, y + h // 2))
        screen=self._screen
        screen.blit(rotated_rect, rect.topleft)

    def _draw_rect(self):
        offset_x=self._parent._offset_x
        offset_y=self._parent._offset_y
        x=(self._x - offset_x) * self._scale
        y=(self._y - offset_y) * self._scale
        w=self._width * self._scale
        h=self._height * self._scale
        self.rotateRect(x,y,w,h,self.__BLUE,self._startrotation)


    def _draw_hitbox(self):
        offset_x=self._parent._offset_x
        offset_y=self._parent._offset_y
        x=(self._x+self._hitbox_x - offset_x) * self._scale
        y=(self._y+self._hitbox_y - offset_y) * self._scale
        w=self._hitbox_width * self._scale
        h=self._hitbox_height * self._scale
        self.rotateRect(x,y,w,h,self.__RED,self._startrotation)

    def _draw_onscreen(self,x,y,w,h):
        image=self._tile._image
        image=self._pygame.transform.scale(image, (w, h))
        screen=self._screen
        
        rot=self._startrotation #in grad
        if rot:
            rotated_image=self._pygame.transform.rotate(image, rot)
            image_rect= rotated_image.get_rect(center=image.get_rect(topleft=(x, y)).center)
            screen.blit(rotated_image, image_rect) 
        else:
            #rotated_image = pygame.transform.rotate(image, 45)
            screen.blit(image, (x, y)) 


    def _draw_image(self):
        if (self._tile._image == None):
            return
        offset_x=self._parent._offset_x
        offset_y=self._parent._offset_y 
        x=(self._x - offset_x) * self._scale  + self._screen.get_width()/2
        y=(self._y - offset_y) * self._scale + self._screen.get_height()/2

        # x=(self._x * self._scale - offset_x) 
        # y=(self._y * self._scale - offset_y) 
        
        w=self._width * self._scale
        h=self._height * self._scale
        
        self._draw_onscreen(x,y,w,h)


    def update_player(self):
        w=self._width * self._scale
        h=self._height * self._scale
        x=self._screen.get_width() / 2 - w / 2
        y=self._screen.get_height() / 2 - h / 2
        self._draw_onscreen(x,y,w,h)



    def update(self):
        #print("Update")
        self._draw_image()
        if (self._dev):
            self._draw_rect()
            self._draw_hitbox()
        
        #print (screen._offset_x)
        #print (self._parent._offset_x)

    def getX(self):
        return 

		

	
