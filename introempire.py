import ui, net, app, dbg

kingdoms = {
	1 : {"name" : "Βασίλειο του Shinsoo",
		"desc" : [
			"Το Βασίλειο του Shinsoo",
			"βρίσκεται στα νότια της ηπείρου.",
			"Η κύρια ενασχόληση των κατοίκων",
			"Είναι το εμπόριο. Οι εμπορικές σχέσεις",
			"με την Ανατολή εξελίχθηκαν γρήγορα.",
		]},
	2 : {"name" : "Βασίλειο του Chunjo",
		"desc" : [
			"Το Βασίλειο του Chunjo",
			"βρίσκεται στα δυτικά της Ηπείρου.",
			"Είναι θεοκρατικό βασίλειο και διοικείται",
			"από τους πνευματικούς του Ηγέτες.",
			"Το Βασίλειο ιδρύθηκε από τον Yoon-Young.",
		]},
	3 : {"name" : "Βασίλειο του Jinno",
		"desc" : [
			"Το Βασίλειο του Jinno",
			"Είναι στις ανατολικές περιοχές της ηπείρου. ",
			"Το βασίλειο στηρίζεται στη στρατιωτική δύναμη,",
			"Οι άνθρωποί του είναι επιθετικοί και μαχητές.",
			"Το Βασίλειο είναι υπό την ηγεσία Ee-Ryoong.",
		]},
}

class SelectEmpireWindow(ui.ScriptWindow):

	def __init__(self, stream = None):
		ui.ScriptWindow.__init__(self)
		self.stream = stream
		self.id = 1
		self.__LoadScript("sistimata/code/ui_jack_kingdom.py")
		self.ChangeEmpire("init")
				
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Open(self):
		self.Show()
		app.ShowCursor()
		
	def Close(self):
		self.Hide()
		app.HideCursor()
		self.exitButton = None

	def __LoadScript(self, fileName):
		try:
			pyLoader = ui.PythonScriptLoader()
			pyLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("poccix_kingdom.py ## __LoadScript.LoadScriptFile")
		try:
			GetObject=self.GetChild
			self.exitButton = GetObject("exit_button")
			self.kingdom = {
				1 : self.GetChild("kingdom_01"),
				2 : self.GetChild("kingdom_02"),
				3 : self.GetChild("kingdom_03"),
			}
			self.btn_select = {
				0 : self.GetChild("btn_select_01"),
				1 : self.GetChild("btn_select_02"),
				2 : self.GetChild("btn_select_03"),
			}
			self.texts = {
				1 : {
					0 : self.GetChild("text_kingdom_01_01"),
					1 : self.GetChild("text_kingdom_01_02"),
					2 : self.GetChild("text_kingdom_01_03"),
					3 : self.GetChild("text_kingdom_01_04"),
					4 : self.GetChild("text_kingdom_01_05"),
				},
				2 : {
					0 : self.GetChild("text_kingdom_02_01"),
					1 : self.GetChild("text_kingdom_02_02"),
					2 : self.GetChild("text_kingdom_02_03"),
					3 : self.GetChild("text_kingdom_02_04"),
					4 : self.GetChild("text_kingdom_02_05"),
				},
				3 : {
					0 : self.GetChild("text_kingdom_03_01"),
					1 : self.GetChild("text_kingdom_03_02"),
					2 : self.GetChild("text_kingdom_03_03"),
					3 : self.GetChild("text_kingdom_03_04"),
					4 : self.GetChild("text_kingdom_03_05"),
				},
			}
		except:
			import exception
			exception.Abort("poccix_kingdom.py ## __LoadScript.GetChild")
		try:
			for selid in range(len(self.btn_select)):
				self.btn_select[selid].SetEvent(ui.__mem_func__(self.SelectEmpire), selid+1)
		except:
			import exception
			exception.Abort("poccix_kingdom.py ## __LoadScript.SetEvent")

		self.exitButton.SetEvent(ui.__mem_func__(self.CloseBtn))

	def ChangeEmpire(self, count):
		if count == "init":
			pass
		
		for j in range(len(self.texts)):
			for i in range(len(self.texts[j+1])):
				self.texts[j+1][i].SetText(kingdoms[j+1]["desc"][i])

	def SelectEmpire(self, selid):
		net.SendSelectEmpirePacket(self.id)
		self.stream.SetSelectCharacterPhase()
		
	def CloseBtn(self):
		self.stream.SetLoginPhase()
			
	def EmptyFunc(self):
		pass
	
	def OnPressExitKey(self):
		self.CloseBtn()

	def OnKeyDown(self, key):
		if key == app.DIK_ESC:
			self.stream.SetLoginPhase()

class ReselectEmpireWindow(SelectEmpireWindow):
	def SelectEmpire(self, selid):
		net.SendSelectEmpirePacket(selid)
		self.stream.SetCreateCharacterPhase()

	def CloseBtn(self):
		self.stream.SetLoginPhase()
