import app
import net
import ui
import snd
import wndMgr
import musicInfo
import systemSetting
import localeinfo
import constInfo
import ime
import serverInfo
from _weakref import proxy

import _winreg
REG_PATH = r"SOFTWARE\Nirvana"

def set_reg(name, value):
	try:
		_winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
		registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)
		_winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
		_winreg.CloseKey(registry_key)
		return True
	except WindowsError:
		return False

def get_reg(name):
	try:
		registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_READ)
		value, regtype = _winreg.QueryValueEx(registry_key, name)
		_winreg.CloseKey(registry_key)
		return str(value)
	except WindowsError:
		return None		
		
class LoginWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.stream = stream	
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)

	def Open(self):
		self.loginFailureMsgDict={

			"ALREADY"	: localeinfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeinfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeinfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeinfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeinfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeinfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeinfo.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: localeinfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeinfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeinfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeinfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeinfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeinfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeinfo.LOGIN_FAILURE_WEB_BLOCK,
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: localeinfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"WRONGMAT"	: localeinfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		self.__LoadScript("sistimata/interface/loginwindow/loginwindow.py")
		
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("miles/BGM/" + musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())
		self.CheckAccount()

		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
		self.SetChannel(0)
		
		self.Show()
		app.ShowCursor()	

	def Close(self):
		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("miles/BGM/"+musicInfo.loginMusic)
	
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
	
		self.Hide()
		app.HideCursor()
		ime.ClearExceptKey()

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeinfo.LOGIN_CONNECT_FAILURE, self.EmptyFunc)

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeinfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeinfo.LOGIN_PROCESSING)

	def OnLoginFailure(self, error):
		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
		
			loginFailureMsg = localeinfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc = self.loginFailureFuncDict.get(error, self.EmptyFunc)

		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			self.idEditLine = self.GetChild("id")
			self.pwdEditLine = self.GetChild("pwd")
			self.pinEditLine = self.GetChild("pin")
			self.loginButton = self.GetChild("login_button")
			self.exitButton = self.GetChild("exit_button")
			
			self.channelButton = {
				0 : self.GetChild("ch1"),
				1 :	self.GetChild("ch2"),
				2 : self.GetChild("ch3"),
				3 : self.GetChild("ch4"),
				4 : self.GetChild("ch5"),
				5 : self.GetChild("ch6")}
			
			self.accountData = {
				0 : [[self.GetChild("load_button_0"), self.GetChild("save_button_0"), self.GetChild("delete_button_0")], self.GetChild("account_0_text")],
				1 : [[self.GetChild("load_button_1"), self.GetChild("save_button_1"), self.GetChild("delete_button_1")], self.GetChild("account_1_text")],
				2 : [[self.GetChild("load_button_2"), self.GetChild("save_button_2"), self.GetChild("delete_button_2")], self.GetChild("account_2_text")],
				3 : [[self.GetChild("load_button_3"), self.GetChild("save_button_3"), self.GetChild("delete_button_3")], self.GetChild("account_3_text")]}

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")
			
		for (key, item) in self.accountData.items():
			if isinstance(item[0], list):
				item[0][0].SetEvent(ui.__mem_func__(self.LoadAccount), key)
				item[0][1].SetEvent(ui.__mem_func__(self.SaveAccount), key)
				item[0][2].SetEvent(ui.__mem_func__(self.DeleteAccount), key)
				
		for (channelID, channelButtons) in self.channelButton.items():
				channelButtons.SetEvent(ui.__mem_func__(self.SetChannel), channelID)

		self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.exitButton.SetEvent(ui.__mem_func__(self.OnPressExitKey))
		
		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))

		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		if app.ENABLE_CHECK_CLIENT_VERSION_SERVER_AND_PIN:
			self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.pinEditLine.SetFocus))
		else:
			self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))

		if app.ENABLE_CHECK_CLIENT_VERSION_SERVER_AND_PIN:
			self.pinEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
			self.pinEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))

	def CheckAccount(self):
		for i in xrange(4):
			if get_reg("id_%d" % i):
				self.accountData[i][1].SetText(str(get_reg("id_%d" % i)))
				self.accountData[i][0][1].Hide()
				self.accountData[i][0][0].Show()
			else:
				self.accountData[i][1].SetText(localeinfo.KENI_THESI)
				self.accountData[i][0][1].Show()
				self.accountData[i][0][0].Hide()
				
	def DeleteAccount(self, key):
		if get_reg("id_%d" % key):
			set_reg("id_%d" % key, "")
			set_reg("pwd_%d" % key, "")
			set_reg("pin_%d" % key, "")
			self.PopupNotifyMessage(localeinfo.DIAGRAFI_THESI)
		else:
			self.PopupNotifyMessage(localeinfo.DIAGRAFI_LATHOS)
			
		self.CheckAccount()
		
	def LoadAccount(self, key):
		if get_reg("id_%d" % key):
			self.idEditLine.SetText(str(get_reg("id_%d" % key)))
			self.pwdEditLine.SetText(str(get_reg("pwd_%d" % key)))
			self.pwdEditLine.SetFocus()
			self.pinEditLine.SetText(str(get_reg("pin_%d" % key)))
			self.pinEditLine.SetFocus()
		else:
			self.PopupNotifyMessage(localeinfo.DIAGRAFI_LATHOS_B)
			
	def SaveAccount(self, key):
		if get_reg("id_%d" % key):
			self.PopupNotifyMessage(localeinfo.DIAGRAFI_LATHOS_DEZ)
			return
		
		if self.idEditLine.GetText() == "" or self.pwdEditLine.GetText() == "" or self.pinEditLine.GetText() == "":
			self.PopupNotifyMessage(localeinfo.DIAGRAFI_LATHOS_BEDUG)
			return
		
		set_reg("id_%d" % key, self.idEditLine.GetText())
		set_reg("pwd_%d" % key, self.pwdEditLine.GetText())
		set_reg("pin_%d" % key, self.pinEditLine.GetText())
		self.PopupNotifyMessage(localeinfo.OKEYACCOUNT)
		self.CheckAccount()

	def SetChannel(self, ch):
		for key, button in self.channelButton.items():
			button.SetUp()
			
		self.channelButton[ch].Down()

		self.stream.SetConnectInfo(serverInfo.SERVER_IP, self.ChannelPort(ch, 0), serverInfo.SERVER_IP, self.ChannelPort("LOGIN"))
		net.SetMarkServer(serverInfo.SERVER_IP, self.ChannelPort("LOGO"))
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")
		net.SetServerInfo(self.ChannelPort(ch, 2))
		
	def ChannelPort(self, ch, value=0):
		channel = {

			0	:	serverInfo.CH1_PORT,
			1	:	serverInfo.CH2_PORT,
			2	:	serverInfo.CH3_PORT,
			3	:	serverInfo.CH4_PORT,
			4	:	serverInfo.CH5_PORT,
			5	:	serverInfo.CH6_PORT}
		
		if ch == "LOGIN":
			return serverInfo.PORT_AUTH
		elif ch == "LOGO":
			return channel[0]
		elif value == 2:
			return serverInfo.NUME_SERVER % (ch+1)
		else:
			return channel[ch]
				
	def Connect(self, id, pwd, pin):
		constInfo.LastAccount = id.lower()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeinfo.LOGIN_CONNETING, self.EmptyFunc, localeinfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd, pin)
		self.stream.Connect()
		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeinfo.UI_OK)

	def OnPressExitKey(self):
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def EmptyFunc(self):
		pass

	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()
		pin = self.pinEditLine.GetText()

		if len(id)==0:
			self.PopupNotifyMessage(localeinfo.LOGIN_INPUT_ID, self.EmptyFunc)
			return

		if len(pwd)==0 or len(pin)==0:
			self.PopupNotifyMessage(localeinfo.LOGIN_INPUT_PASSWORD, self.EmptyFunc)
			return

		self.Connect(id, pwd, pin)

