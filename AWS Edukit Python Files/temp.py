lcd.font(lcd.FONT_DejaVu24)
lcd.setTextColor(0xffffff,lcd.ORANGE)
lcd.fillRoundRect(40,90,240,60,10,lcd.ORANGE)
lcd.print("Reseting...",86,110)
from utils import filecp
filecp('apps/main.py', 'main.py')
core_start('app')
machine.reset()