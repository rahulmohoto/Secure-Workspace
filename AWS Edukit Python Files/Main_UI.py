from GlobalLibrary import *

class UI:
  
  screen = None
  
  def __init__(self, screen):
    self.screen = screen
    self.screen.set_screen_bg_color(0x0b0b0b)
    M5Img("res/SecureWorkspace.png", x=0, y=0, parent=None)

