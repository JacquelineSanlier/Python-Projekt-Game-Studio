
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
	_id:int = 0               #unique ID
	_interactive:bool = False #0 Not inteeractive 1 with collision
	_src: str = ""            #Image file
	_name:str = ""            #ZB "Baum"
	_x:int = 0                #Position X
	_y:int = 0                #Position Y
	_width:int = 0            #Width 
	_height:int = 0           #Height
	_tile_item=None           #has the src of the Image
	
	_dx:int =0				  #movement per 1/60s  -1 left +1 right 0 no move
	_dy:int =0                #movement per 1/60s  -1 up   +1 down  0 no move
	
	_collisionbox_x:int = 0                #Collision Position X
	_collisionbox_y:int = 0                #Collision Position Y
	_collisionbox_width:int = 0            #Collision Width 
	_collisionbox_height:int = 0           #Collision Height
	
	def __init__(self,id,name,tile_item,x,y,width,height):
		self._id=id
		self._name=name
		self._x=x
		self._y=y
		self._width=width
		self._height=height
		self._tile_item=tile_item
		
	def setPosition(self,x,y):
		self._x=x
		self._y=y

	def setSize(self,width,height):
		self._width=width
		self._height=height

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
        
	
