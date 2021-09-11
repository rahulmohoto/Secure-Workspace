from GlobalLibrary import *
from WelcomePage import Welcome
from LoginPage import LoginDashboard
from Registration import GetRegistered
from GetfromAWS import getDataAWS
from ViewProfile import Profile
from SOSMessage import SOS
from Main_UI import UI
from ble import ble_uart

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xdddcdc)
screen.set_screen_brightness(30)

ui_screen = UI(screen)
user_info = getDataAWS()

uart_ble = None

def set_user_profile(user_info, screen):
    user_profile = Profile(screen, user_info)
    if user_profile.getClicked():
        if user_profile.get_Edit_Clicked():
            GetRegistered(screen, 2)
            del user_profile
            return True
        if user_profile.get_btnA_clicked():
            del user_profile
            return False

def set_login(user_info, screen):
    login = LoginDashboard(user_info, screen)
    if login.getClicked():
        if login.get_Profile_Button_Clicked():
            set_user_profile(user_info, screen)
            return
        if login.get_SOS_Button_Clicked():
            sos_message = SOS(screen, uart_ble, user_info["Message"])
            if sos_message.get_btnA_clicked():
                del sos_message
                return

del ui_screen
screen.clean_screen()
screen.set_screen_bg_color(0xdddcdc)

if user_info is None:
    welcome = Welcome()
    welcome.wait_for_button_press()
    del welcome
    user_info = GetRegistered(screen, 1)
    screen.clean_screen()
    uart_ble = ble_uart.init(user_info["Name_Data"])
    while True:
      set_login(user_info, screen)
      screen.clean_screen()
else:
    uart_ble = ble_uart.init(user_info["Name_Data"])
    while True:
      set_login(user_info, screen)
      screen.clean_screen()