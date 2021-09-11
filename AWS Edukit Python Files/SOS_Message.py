from GlobalLibrary import *

class SOS:

    isBtnAClicked = btnA = screen = uart_ble = None

    def __init__(self, screen, uart_ble, message):
        isBtnAClicked = False
        self.btnA = btnA
        self.screen = screen
        self.uart_ble = uart_ble
        self.screen.clean_screen()
        M5Label('Sending SOS message', x=50, y=110, color=0xfa0606, font=FONT_MONT_20, parent=None)
        M5Line(x1=26, y1=139, x2=296, y2=139, color=0x000, width=2, parent=None)
        rgb.setColorAll(0xff0000)
        speaker.playWAV("res/Alarm.wav")
        uart_ble.write(message)

    def buttonA_wasPressed(self):
        self.isBtnAClicked = True
        rgb.setColorAll(0x000000)

    def get_btnA_clicked(self):
        while self.isBtnAClicked != True:
            self.btnA.wasPressed(self.buttonA_wasPressed)

    