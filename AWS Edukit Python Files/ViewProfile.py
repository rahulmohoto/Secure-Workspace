from GlobalLibrary import *

class Profile:

    screen = user_info = edit_button = isEditClicked = isBtnAClicked = btnA = None

    def edit_button_pressed(self):
        self.isEditClicked = True
    
    def buttonA_wasPressed(self):
        self.isBtnAClicked = True

    def __init__(self, screen, user_info):
        self.screen = screen
        self.user_info = user_info
        self.screen.clean_screen()
        self.isEditClicked = False
        self.isBtnAClicked = False
        self.btnA = btnA

        self.edit_button = M5Btn(text='Edit', x=220, y=165, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
        M5Line(x1=110, y1=43, x2=210, y2=43, color=0x000, width=2, parent=None)
        M5Label('Profile', x=130, y=17, color=0x000, font=FONT_MONT_18, parent=None)
        M5Label('Name: '+self.user_info["Name_Data"], x=26, y=70, color=0xfa0404, font=FONT_MONT_14, parent=None)
        M5Label('Password: '+self.user_info["Password"], x=26, y=100, color=0xf70606, font=FONT_MONT_14, parent=None)
        M5Label('Message: '+self.user_info["Message"], x=26, y=130, color=0xf70606, font=FONT_MONT_14, parent=None)

    def getClicked(self):
        while True:
            self.edit_button.pressed(self.edit_button_pressed)
            self.btnA.wasPressed(self.buttonA_wasPressed)

            if self.isEditClicked or self.isBtnAClicked:
                break
        return True
    
    def get_Edit_Clicked(self):
        return self.isEditClicked

    def get_btnA_clicked(self):
        return self.isBtnAClicked
        