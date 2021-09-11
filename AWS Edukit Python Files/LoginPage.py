from GlobalLibrary import *
from ble import ble_uart

class LoginDashboard:

    sosButton = profileButton = user_info = screen = isClickedProfile = isClickedSOS = None

    def profileButton_pressed(self):
        self.isClickedProfile = True

    def sosButton_pressed(self):
        self.isClickedSOS = True

    def __init__(self, user_info, screen):
        self.user_info = user_info
        self.screen = screen
        self.isClickedProfile = False
        self.isClickedSOS = False

        self.profileButton = M5Btn(text='My Profile', x=110, y=85, w=100, h=40, bg_c=0xeae0e0, text_c=0x000000, font=FONT_MONT_14, parent=None)
        self.sosButton = M5Btn(text='SOS', x=90, y=160, w=140, h=50, bg_c=0xfc0505, text_c=0x000000, font=FONT_MONT_14, parent=None)
        M5Label('Dashboard', x=110, y=17, color=0x000, font=FONT_MONT_18, parent=None)
        M5Line(x1=100, y1=43, x2=217, y2=43, color=0x000, width=2, parent=None)
        M5Label('Hi '+self.user_info["Name_Data"]+', see your profile here', x=72, y=60, color=0x000, font=FONT_MONT_12, parent=None)
        M5Label('Send emmergency message', x=76, y=138, color=0x000, font=FONT_MONT_12, parent=None)

    def getClicked(self):
        while True:
            self.sosButton.pressed(self.sosButton_pressed)
            self.profileButton.pressed(self.profileButton_pressed)

            if self.isClickedProfile or self.isClickedSOS:
                break
        return True

    def get_Profile_Button_Clicked(self):
        return self.isClickedProfile

    def get_SOS_Button_Clicked(self):
        return self.isClickedSOS



