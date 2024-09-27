import pygame

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

    #takes ID, parent relative percentage witch and height, parent relative position, parent relative positon y, and either display or another rect as parent.
    def __init__(self, _new_id: int, _parent_window: pygame.Surface, _perc_width: int= 100, _perc_height: int = 100, _pos_x: int = 0, _pos_y: int = 0, _centered = False):

        if not _parent_window:
            raise RuntimeError("No parent given, can not use Canvas - style UI")
        
        if type(_parent_window) is WindowBase:
            self._parent = _parent_window._surface
            _parent_window = _parent_window._surface

        self._parent = _parent_window
        self._parent_dimensions = [_parent_window.get_width(),_parent_window.get_height()]

        self._id = _new_id
        self._width = int(self._parent_dimensions[0]*(_perc_width/100))
        self._height = int(self._parent_dimensions[1]*(_perc_height/100))

        if _centered:
            _pos_x = _pos_x - int(self._width/2)
            _pos_y = _pos_y - int(self._height/2)

        #preconstrcuct rectangle
        self._rect = pygame.Rect(_pos_x, _pos_y, self._width, self._height)
        #use rectangle to make surface
        self._surface = pygame.Surface((self._rect.width, self._rect.height))
        self._surface.fill((0,0,0,0))
    
    def update(self):
        if self._unblitted:
            self._parent.blit(self._surface, (0,0))
        pygame.draw.rect(self._parent, self._color, self._rect)