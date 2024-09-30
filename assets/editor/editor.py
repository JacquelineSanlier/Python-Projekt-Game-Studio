from editorcontroller import Editorcontroller
from editorgui import Editorgui 


if __name__ == "__main__":  
    controller=Editorcontroller()
    gui=Editorgui(controller)
    controller.setGui(gui)
    gui.startGui()

