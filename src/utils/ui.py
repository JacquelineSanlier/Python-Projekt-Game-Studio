import pygame

pygame.font.init()
fontsmall = pygame.font.SysFont("monospace", 15)
fontmid = pygame.font.SysFont("monospace", 25)
fontbig = pygame.font.SysFont("monospace", 35)

class WindowBase: #used for any window that can have subwindows and segments
    _id: int
    _width: int
    _height: int
    _rect: pygame.Rect
    _surface: pygame.Surface
    _parent = None
    _parent_dimensions = None
    _color = pygame.Color(255,255,255,100)
    _unblitted = True

    #takes ID, parent, relative percentage witch and height, relative position x and positon y. should draw and keep track of rects created this way
    def __init__(self, _new_id: int, _main_surface: pygame.Surface, _perc_width: int= 100, _perc_height: int = 100, _pos_x: int = 0, _pos_y: int = 0, _centered = False):

        if not _main_surface:
            raise RuntimeError("No parent given, can not use Canvas - style UI")
        
        if type(_main_surface) is not pygame.Surface:
            raise RuntimeError("Needs Surface to Draw UI!")

        self._parent = _main_surface
        self._parent_dimensions = [_main_surface.get_width(),_main_surface.get_height()]

        self._id = _new_id
        self._width = int(self._parent_dimensions[0]*(_perc_width/100))
        self._height = int(self._parent_dimensions[1]*(_perc_height/100))

        if _centered:
            _pos_x = _pos_x - int(self._width/2)
            _pos_y = _pos_y - int(self._height/2)

        #preconstrcuct rectangle
        self._rect = pygame.Rect(_pos_x, _pos_y, self._width, self._height)

    
    def update(self):
        pygame.draw.rect(self._parent, self._color, self._rect)

    def close(self): #destroys the window
        del self

class TextBase:
    _id: int
    _text: str
    _parent: pygame.Surface
    _x: int
    _y: int
    _fontsize: int #1 2 or 3

    #takes id , the text to display, the parent window which should always be our main, x and Y pos ,as well as a font size between 1 and 3
    def __init__(self , _id:int , _text: str, _parent: pygame.Surface, _pox_x: int, _pos_y: int, _fontsize = 1):
        self._id = _id
        self._text = _text
        self._parent = _parent
        self._x = _pox_x
        self._y = _pos_y
        self._fontsize = _fontsize

    #takes new text to update the text display
    def update(self, _text_new = ""):

        if _text_new != self._text and _text_new != "":
            self._text = _text_new

        match self._fontsize:
            case 1:
                font = fontsmall
            case 2:
                font = fontmid
            case 3:
                font = fontbig

        render_text = font.render(self._text, 1, (255,255,255))
        self._parent.blit(render_text, (self._x, self._y))