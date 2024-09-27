
#
# Images than are use in the game
# can be used on more places
# an enmy can look the same, a tree too
#
# we cann add movements,sequences  here or better in an other class where like:
# dieing, jumping, falling, landing, walking 
# 

class tile_item:
	#_id:int=0        # id 
	#_src:str =""     # path
	#_name:str =""    # name caan be found by Name  
	

	#
	# Initialise and give 
	#
    def __init__(self,id,name,src):
        self._id    = id
        self._name  = name
        self._src   = src

	
# Tile = Item auf dem Bildschirm , Entity = Interagierendes Item
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
	_tile_item=None           #has the src of the Image

	
	
	_dx:int =0				  #movement per 1/60s  -1 left +1 right 0 no move
	_dy:int =0                #movement per 1/60s  -1 up   +1 down  0 no move
	
	_hitbox_x:int = 0                #Collision Position X
	_hitbox_y:int = 0                #Collision Position Y
	_hitbox_width:int = 0            #Collision Width 
	_hizbox_height:int = 0           #Collision Height
	__TRANSPARENT = (0,0,0,0)        #Transparenter Hintergrund 0-255
	__BLUE        = (0,0,255,255)    #Transparenter Hintergrund 0-255
	__RED         = (255,0,0,255)    #Transparenter Hintergrund 0-255
	
	# Erstelle eine Surface mit Transparenz
	#transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
	#transparent_surface.fill(BLUE)  # Fülle die Surface mit transparenter Farbe
	# Zeichne die transparente Surface
    #screen.blit(transparent_surface, (rect_x, rect_y))
    

	def __init__(self,pygame,screen,id,tile_item=None):
		self._id=id
		self._tile_item=tile_item
		self._pygame=pygame
		self._screen=screen

	def _getX(self):
		print("Hallo")
		print(self._x)

	def getY(self):
		print("Hallo Y")

	def setId(self,id):
		self._id=id

	def setName(self,name):
		self._name=name

	def setPosition(self,x,y):
		self._x=x
		self._y=y
		self.hitbox_x=x
		self.hitbox_y=y

	def setSize(self,width,height):
		self._width=width
		self._height=height
		self._hitbox_width=width
		self._hitbox_height=height

	def setHitbox(self,x,y,width,height):
		self.hitbox_x=x
		self.hitbox_y=y
		self._hitbox_width=width
		self._hitbox_height=height

	def setScale(self,scale):
		self._scale=scale

	def setMove(self,dx,dy):
		self._dx=dx
		self._dy=dy
		
	def move(x,y):

		#remove old from screen
		pass

	def remove():
		pass

	def hide():
		pass

	def collides():
		pass
    
	def _draw_rect(self):
		x=self._x * self._scale
		y=self._y * self._scale
		w=self._width
		h=self._height
		screen=self._screen
		# self._pygame.draw.rect(screen,self.__BLUE,(x,y,w,h),2)
		self._pygame.draw.rect(screen,(0,0,255),(x,y,w,h))

	def _draw_hitbox(self):
		x=self._hitbox_x * self._scale
		y=self._hitbox_y * self._scale
		w=self._hitbox_width
		h=self._hitbox_height
		screen=self._screen
		return
		self._pygame.draw.rect(screen,self.__RED,(x,y,w,h),1)

	def _draw_image(self):
		return
		x=self._x * self._scale
		y=self._y * self._scale
		w=self._width
		h=self._height
		screen=self._screen

	def update(self):
		return
		self._draw_rect()
		#self._draw_hitbox()
		#self._draw_image()


		

	
