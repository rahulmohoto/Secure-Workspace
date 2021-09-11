from GlobalLibrary import *

class Welcome:

    setup = screen = setup_button = None

    def setup_button_pressed(self):
        self.setup = 1

    def __init__(self):
        self.setup = 0
        self.setup_button = M5Btn(text='Setup', x=122, y=200, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

        M5Line(x1=25, y1=60, x2=240, y2=60, color=0x000, width=2, parent=None)
        M5Label('Secure Workspace', x=25, y=30, color=0x000, font=FONT_MONT_18, parent=None)
        M5Label('Are you stuck somewhere?', x=26, y=70, color=0xfa0404, font=FONT_MONT_14, parent=None)
        M5Label('Cannot find exit?', x=26, y=130, color=0xfd0404, font=FONT_MONT_14, parent=None)
        M5Label('You are one click away to get help', x=26, y=175, color=0x0e05f9, font=FONT_MONT_16, parent=None)
        M5Line(x1=26, y1=172, x2=295, y2=172, color=0x040404, width=2, parent=None)
        M5Label('Need emergency assistance?', x=26, y=150, color=0xfc0303, font=FONT_MONT_14, parent=None)
        M5Label('Has fire spread out?', x=26, y=90, color=0xf70606, font=FONT_MONT_14, parent=None)
        M5Label('Has the building collapsed?', x=26, y=110, color=0xf70606, font=FONT_MONT_14, parent=None)

    def wait_for_button_press(self):
        while True and self.setup!=1:
            self.setup_button.pressed(self.setup_button_pressed)
