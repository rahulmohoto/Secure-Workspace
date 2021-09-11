from GlobalLibrary import *

class Keyboard_Registration:

	click = 0 #for Maping and key function
	inputField = "" #for input
	clickCount = 0 #for clicking count

	S_Z_Button = OkButton = RegistrationWelcome = NameLabel = InputTextLabel = screen = None

	DictionaryOfAlphabetLabels = {} 

	DictionaryOfAtoF={"Letter":['A','B','C','D','E','F'],"X1":['0','54','107','160','213','266'],"X2":['53','106','159','212','265','320']}
	DictionaryOfGtoL={"Letter":['G','H','I','J','K','L'],"X1":['0','54','107','160','213','266'],"X2":['53','106','159','212','265','320']}
	DictionaryOfMtoR={"Letter":['M','N','O','P','Q','R'],"X1":['0','54','107','160','213','266'],"X2":['53','106','159','212','265','320']}
	DictionaryOfStoX={"Letter":['S','T','U','V','W','X'],"X1":['0','54','107','160','213','266'],"X2":['53','106','159','212','265','320']}
	DictionaryOfYto4={"Letter":['Y','Z','1','2','3','4'],"X1":['0','54','107','160','213','266'],"X2":['53','106','159','212','265','320']}
	DictionaryOf5to0={"Letter":['5','6','7','8','9','0'],"X1":['0','54','107','160','213','266'],"X2":['53','106','159','212','265','320']}

	def __init__(self, screen):

		self.screen = screen
		self.screen.clean_screen()

		self.S_Z_Button = M5Btn(text='S - Z', x=6, y=86, w=50, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
		self.OkButton = M5Btn(text='Next', x=60, y=86, w=50, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

		self.RegistrationWelcome = M5Label('Registration', x=104, y=10, color=0x000, font=FONT_MONT_18, parent=None)
		self.line0 = M5Line(x1=99, y1=35, x2=219, y2=35, color=0x000, width=2, parent=None)
		self.NameLabel = M5Label('Your Name', x=31, y=53, color=0x000, font=FONT_MONT_14, parent=None)
		self.line1 = M5Line(x1=120, y1=62, x2=130, y2=62, color=0x000, width=2, parent=None)
		self.InputTextLabel = M5Label('eg. RAHUL', x=145, y=53, color=0x7a7979, font=FONT_MONT_14, parent=None)

		M5Line(x1=0, y1=120, x2=320, y2=120, color=0x000, width=1, parent=None)
		M5Line(x1=0, y1=160, x2=320, y2=160, color=0x000, width=1, parent=None)
		M5Line(x1=0, y1=200, x2=320, y2=200, color=0x000, width=1, parent=None)
		M5Line(x1=0, y1=240, x2=320, y2=240, color=0x000, width=1, parent=None)
		M5Line(x1=53, y1=120, x2=53, y2=240, color=0x000, width=1, parent=None)
		M5Line(x1=106, y1=120, x2=106, y2=240, color=0x000, width=1, parent=None)
		M5Line(x1=159, y1=120, x2=159, y2=240, color=0x000, width=1, parent=None)
		M5Line(x1=212, y1=120, x2=212, y2=240, color=0x000, width=1, parent=None)
		M5Line(x1=265, y1=120, x2=265, y2=240, color=0x000, width=1, parent=None)
		M5Line(x1=265, y1=86, x2=320, y2=86, color=0x000, width=1, parent=None)
		M5Line(x1=265, y1=86, x2=265, y2=120, color=0x000, width=1, parent=None)

		ClearLabel = M5Label('Clear', x=278, y=97, color=0x000, font=FONT_MONT_14, parent=None)

		self.DictionaryOfAlphabetLabels["ALabel"] = M5Label('', x=21, y=133, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["BLabel"] = M5Label('', x=74, y=133, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["CLabel"] = M5Label('', x=126, y=133, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["DLabel"] = M5Label('', x=177, y=133, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["ELabel"] = M5Label('', x=234, y=133, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["FLabel"] = M5Label('', x=285, y=133, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["GLabel"] = M5Label('', x=19, y=170, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["HLabel"] = M5Label('', x=73, y=170, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["ILabel"] = M5Label('', x=131, y=170, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["JLabel"] = M5Label('', x=179, y=170, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["KLabel"] = M5Label('', x=234, y=170, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["LLabel"] = M5Label('', x=285, y=170, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["MLabel"] = M5Label('', x=20, y=212, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["NLabel"] = M5Label('', x=74, y=212, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["OLabel"] = M5Label('', x=126, y=212, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["PLabel"] = M5Label('', x=178, y=212, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["QLabel"] = M5Label('', x=232, y=212, color=0x000, font=FONT_MONT_14, parent=None)
		self.DictionaryOfAlphabetLabels["RLabel"] = M5Label('', x=285, y=212, color=0x000, font=FONT_MONT_14, parent=None)


		lcd.rect(140, 45, 150, 30, color=0xcc0000)