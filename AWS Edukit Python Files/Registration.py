from GlobalLibrary import *
from m5stack import touch
from KeyboardVariables import Keyboard_Registration
from SendtoAWS import SavetoAWS,EditonAWS
from m5stack import touch

obj = None #Later we will define it as an object of KeyboardVariables class

def A_R_Map():
  global obj

  obj.DictionaryOfAlphabetLabels["ALabel"].set_text('A')
  obj.DictionaryOfAlphabetLabels["BLabel"].set_text('B')
  obj.DictionaryOfAlphabetLabels["CLabel"].set_text('C')
  obj.DictionaryOfAlphabetLabels["DLabel"].set_text('D')
  obj.DictionaryOfAlphabetLabels["ELabel"].set_text('E')
  obj.DictionaryOfAlphabetLabels["FLabel"].set_text('F')
  obj.DictionaryOfAlphabetLabels["GLabel"].set_text('G')
  obj.DictionaryOfAlphabetLabels["HLabel"].set_text('H')
  obj.DictionaryOfAlphabetLabels["ILabel"].set_text('I')
  obj.DictionaryOfAlphabetLabels["JLabel"].set_text('J')
  obj.DictionaryOfAlphabetLabels["KLabel"].set_text('K')
  obj.DictionaryOfAlphabetLabels["LLabel"].set_text('L')
  obj.DictionaryOfAlphabetLabels["MLabel"].set_text('M')
  obj.DictionaryOfAlphabetLabels["NLabel"].set_text('N')
  obj.DictionaryOfAlphabetLabels["OLabel"].set_text('O')
  obj.DictionaryOfAlphabetLabels["PLabel"].set_text('P')
  obj.DictionaryOfAlphabetLabels["QLabel"].set_text('Q')
  obj.DictionaryOfAlphabetLabels["RLabel"].set_text('R')


def S_Z_Map():
  global obj

  obj.DictionaryOfAlphabetLabels["ALabel"].set_text('S')
  obj.DictionaryOfAlphabetLabels["BLabel"].set_text('T')
  obj.DictionaryOfAlphabetLabels["CLabel"].set_text('U')
  obj.DictionaryOfAlphabetLabels["DLabel"].set_text('V')
  obj.DictionaryOfAlphabetLabels["ELabel"].set_text('W')
  obj.DictionaryOfAlphabetLabels["FLabel"].set_text('X')
  obj.DictionaryOfAlphabetLabels["GLabel"].set_text('Y')
  obj.DictionaryOfAlphabetLabels["HLabel"].set_text('Z')
  obj.DictionaryOfAlphabetLabels["ILabel"].set_text('1')
  obj.DictionaryOfAlphabetLabels["JLabel"].set_text('2')
  obj.DictionaryOfAlphabetLabels["KLabel"].set_text('3')
  obj.DictionaryOfAlphabetLabels["LLabel"].set_text('4')
  obj.DictionaryOfAlphabetLabels["MLabel"].set_text('5')
  obj.DictionaryOfAlphabetLabels["NLabel"].set_text('6')
  obj.DictionaryOfAlphabetLabels["OLabel"].set_text('7')
  obj.DictionaryOfAlphabetLabels["PLabel"].set_text('8')
  obj.DictionaryOfAlphabetLabels["QLabel"].set_text('9')
  obj.DictionaryOfAlphabetLabels["RLabel"].set_text('0')


def Check_Click_A_R():
  global obj

  if obj.click == 1:
    return "break"

def Check_Click_S_Z():
  global obj

  if obj.click == 0:
    return "break"

def S_Z_Button_pressed():
  global obj

  if obj.click == 1:
    obj.S_Z_Button.set_btn_text('S - Z')
    obj.click = 0
    A_R_Map()

  else:
    obj.S_Z_Button.set_btn_text('A - R')
    obj.click = 1
    S_Z_Map()

def A_R_GetKeyValue():
  global obj

  obj.S_Z_Button.pressed(S_Z_Button_pressed)

  while Check_Click_A_R()!="break" and obj.click!=-1:

    x_pos = int(touch.read()[0])
    y_pos = int(touch.read()[1])
    
    if str(touch.status()) == "False":
        y_pos = 1000
    
    if y_pos<120 and (x_pos>=265 and x_pos<=320):
      obj.inputField = obj.inputField[0:len(obj.inputField)-1]
      obj.InputTextLabel.set_text(obj.inputField)

    elif y_pos>120 and y_pos<160:
      for i in range(7):
        if x_pos>=int(obj.DictionaryOfAtoF.get("X1")[i]) and x_pos<=int(obj.DictionaryOfAtoF.get("X2")[i]):
          obj.inputField = obj.inputField + obj.DictionaryOfAtoF.get("Letter")[i]
          obj.InputTextLabel.set_text(obj.inputField)
          wait_ms(2)
          break

    elif y_pos>160 and y_pos<200:
      for i in range(7):
        if x_pos>=int(obj.DictionaryOfGtoL.get("X1")[i]) and x_pos<=int(obj.DictionaryOfGtoL.get("X2")[i]):
          obj.inputField = obj.inputField + obj.DictionaryOfGtoL.get("Letter")[i]
          obj.InputTextLabel.set_text(obj.inputField)
          wait_ms(2)
          break
    
    elif y_pos>200 and y_pos<240:
      for i in range(7):
        if x_pos>=int(obj.DictionaryOfMtoR.get("X1")[i]) and x_pos<=int(obj.DictionaryOfMtoR.get("X2")[i]):
          obj.inputField = obj.inputField + obj.DictionaryOfMtoR.get("Letter")[i]
          obj.InputTextLabel.set_text(obj.inputField)
          wait_ms(2)
          break

    wait_ms(40)

    

def S_Z_GetKeyValue():
  global obj

  obj.S_Z_Button.pressed(S_Z_Button_pressed)

  while Check_Click_S_Z()!="break" and obj.click!=-1:

    x_pos = int(touch.read()[0])
    y_pos = int(touch.read()[1])
    
    if str(touch.status()) == "False":
        y_pos = 1000
    
    if y_pos<120 and (x_pos>=265 and x_pos<=320):
      obj.inputField = obj.inputField[0:len(obj.inputField)-1]
      obj.InputTextLabel.set_text(obj.inputField)

    elif y_pos>120 and y_pos<160:
      for i in range(7):
        if x_pos>=int(obj.DictionaryOfStoX.get("X1")[i]) and x_pos<=int(obj.DictionaryOfStoX.get("X2")[i]):
          obj.inputField = obj.inputField + obj.DictionaryOfStoX.get("Letter")[i]
          obj.InputTextLabel.set_text(obj.inputField)
          wait_ms(2)
          break

    elif y_pos>160 and y_pos<200:
      for i in range(7):
        if x_pos>=int(obj.DictionaryOfYto4.get("X1")[i]) and x_pos<=int(obj.DictionaryOfYto4.get("X2")[i]):
          obj.inputField = obj.inputField + obj.DictionaryOfYto4.get("Letter")[i]
          obj.InputTextLabel.set_text(obj.inputField)
          wait_ms(2)
          break

    elif y_pos>200 and y_pos<240:
      for i in range(7):
        if x_pos>=int(obj.DictionaryOf5to0.get("X1")[i]) and x_pos<=int(obj.DictionaryOf5to0.get("X2")[i]):
          obj.inputField = obj.inputField + obj.DictionaryOf5to0.get("Letter")[i]
          obj.InputTextLabel.set_text(obj.inputField)
          wait_ms(2)
          break

    wait_ms(40)


def OkButton_pressed():
  global obj

  obj.clickCount = obj.clickCount + 1
  
  if obj.clickCount == 1:
    obj.NameLabel.set_text("Password")
    
  elif obj.clickCount == 2:
    obj.NameLabel.set_text("Message")
    obj.OkButton.set_btn_text("OK")
    
  obj.click = -1


def GetRegistered(screen, op_mode):
  
  screen.clean_screen()

  global obj

  obj = Keyboard_Registration(screen)
  
  listOfInputs=[]
  
  for i in range(3):
    
    A_R_Map()
    obj.click = 0
    
    while True and obj.click!=-1:
        obj.OkButton.pressed(OkButton_pressed)
        if obj.click == 1:
            S_Z_GetKeyValue()
        elif obj.click == 0:
            A_R_GetKeyValue()
        
        
    listOfInputs.insert(i, obj.inputField)
    obj.inputField=""
    obj.InputTextLabel.set_text(obj.inputField)
  
  del obj

  DictionaryOfSendingInfo={"Name_Data":listOfInputs[0],"Password":listOfInputs[1],"Message":listOfInputs[2],"Tag":"Send_Data"}
  screen.clean_screen()
  NameLabel = M5Label('Name: '+DictionaryOfSendingInfo["Name_Data"], x=31, y=53, color=0x000, font=FONT_MONT_14, parent=None)
  PasswordLabel = M5Label('Password: '+DictionaryOfSendingInfo["Password"], x=31, y=73, color=0x000, font=FONT_MONT_14, parent=None)
  MessageLabel = M5Label('Message: '+DictionaryOfSendingInfo["Message"], x=31, y=93, color=0x000, font=FONT_MONT_14, parent=None)
  
  RegistrationWelcome2 = M5Label('Registration Completed!', x=51, y=10, color=0x000, font=FONT_MONT_18, parent=None)
  line02 = M5Line(x1=45, y1=35, x2=274, y2=35, color=0x000, width=2, parent=None)
  WaitLabel = M5Label('Wait until we get you to login', x=55, y=135, color=0xfe0404, font=FONT_MONT_14, parent=None)
  OkLabel = M5Label('Your info is saved on AWS. On next', x=28, y=165, color=0x000, font=FONT_MONT_14, parent=None)
  OkLabel2 = M5Label('login, your information will be redirected', x=10, y=185, color=0x000, font=FONT_MONT_14, parent=None)
  OkLabel3 = M5Label('automatically.', x=103, y=205, color=0x000, font=FONT_MONT_14, parent=None)

  # AWS Connection and Publish Message
  if(op_mode == 1):
    SavetoAWS(DictionaryOfSendingInfo)
  else:
    DictionaryOfSendingInfo["Tag"]="Edit_Data"
    EditonAWS(DictionaryOfSendingInfo)
  
  wait(10)
  
  return DictionaryOfSendingInfo


# GetRegistered()