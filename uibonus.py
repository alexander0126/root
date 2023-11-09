import ui
import uiScriptLocale
import app
import net
import dbg
import snd
import player
import mouseModule
import wndMgr
import skill
import playerSettingModule
import quest
import localeinfo
import uiToolTip
import constInfo
import emotion
import chr

SHOW_ONLY_ACTIVE_SKILL = False
SHOW_LIMIT_SUPPORT_SKILL_LIST = []
HIDE_SUPPORT_SKILL_POINT = False


class MenuDialog(ui.ScriptWindow):

	ACTIVE_PAGE_SLOT_COUNT = 8
	SUPPORT_PAGE_SLOT_COUNT = 12

	PAGE_SLOT_COUNT = 12
	PAGE_HORSE = 2

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.state = "STATUS"
		self.isLoaded = 0

		self.toolTipSkill = 0
				
		self.__Initialize()
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.refreshToolTip = 0
		self.curSelectedSkillGroup = 0
		self.canUseHorseSkill = -1

		self.toolTip = None
		self.toolTipJob = None
		self.toolTipAlignment = None
		self.toolTipSkill = None
		self.titleBarDict = None

		self.emotionToolTip = None
		self.soloEmotionSlot = None
		self.dualEmotionSlot = None

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)	
		
	def __BindObject(self):
		self.toolTip = uiToolTip.ToolTip()
		self.toolTipJob = uiToolTip.ToolTip()
		self.toolTipAlignment = uiToolTip.ToolTip(130)	

		self.titleBarDict = {
			"Bonus"		: self.GetChild("Bonus_TitleBar")
		}
		
		global SHOW_ONLY_ACTIVE_SKILL
		global HIDE_SUPPORT_SKILL_POINT

	def __BindEvent(self):

		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.SetCloseEvent(ui.__mem_func__(self.Hide))

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			self.__LoadScript("UIScript/bonuspage.py")
			self.__BindObject()
			self.__BindEvent()
			
			self.GetChild("SwordDef_Value").SetText(str(self.SwordDef()))
			self.GetChild("TwoHandDef_Value").SetText(str(self.TwoHandDef()))
			self.GetChild("DaggerDef_Value").SetText(str(self.DaggerDef()))
			self.GetChild("BellDef_Value").SetText(str(self.BellDef()))
			self.GetChild("FanDef_Value").SetText(str(self.FanDef()))
			self.GetChild("BowDef_Value").SetText(str(self.BowDef()))
			self.GetChild("MagicRes_Value").SetText(str(self.MagicRes()))
			self.GetChild("PointDef_Value").SetText(str(self.PointDef()))
			
			self.GetChild("Block_Value").SetText(str(self.Block()))
			self.GetChild("Dodge_Value").SetText(str(self.Dodge()))			
			self.GetChild("WarriorRes_Value").SetText(str(self.WarriorRes()))
			self.GetChild("NinjaRes_Value").SetText(str(self.NinjaRes()))
			self.GetChild("SuraRes_Value").SetText(str(self.SuraRes()))
			self.GetChild("ShammanRes_Value").SetText(str(self.ShammanRes()))
			self.GetChild("ResToSkillDmg_Value").SetText(str(self.ResToSkillDmg()))
			self.GetChild("AvgDmgRes_Value").SetText(str(self.AvgDmgRes()))
			
			
			self.GetChild("PointAtt_Value").SetText(str(self.PointAtt()))
			self.GetChild("AttHuman_Value").SetText(str(self.AttHuman()))
			self.GetChild("AttAnimals_Value").SetText(str(self.AttAnimals()))
			self.GetChild("AttOrk_Value").SetText(str(self.AttOrk()))
			self.GetChild("AttMilgyo_Value").SetText(str(self.AttMilgyo()))
			self.GetChild("AttUndead_Value").SetText(str(self.AttUndead()))
			self.GetChild("AttDevil_Value").SetText(str(self.AttDevil()))
			self.GetChild("AttMonsters_Value").SetText(str(self.AttMonsters()))
			self.GetChild("Mesi_Value").SetText(str(self.Mesi()))
			self.GetChild("Ikanotitwn_Value").SetText(str(self.Ikanotitwn()))
			self.GetChild("Critical_Value").SetText(str(self.Critical()))
			self.GetChild("Penetrate_Value").SetText(str(self.Penetrate()))
			
			self.GetChild("HPRegen_Value").SetText(str(self.HPRegen()))
			self.GetChild("SPRegen_Value").SetText(str(self.SPRegen()))
			self.GetChild("Poison_Value").SetText(str(self.Poison()))
			self.GetChild("StealHP_Value").SetText(str(self.StealHP()))
			self.GetChild("StealSP_Value").SetText(str(self.StealSP()))
			self.GetChild("AttWarrior_Value").SetText(str(self.AttWarrior()))
			self.GetChild("AttNinja_Value").SetText(str(self.AttNinja()))
			self.GetChild("AttSura_Value").SetText(str(self.AttSura()))
			self.GetChild("AttShaman_Value").SetText(str(self.AttShaman()))
			self.GetChild("EXPdoubleBonus_Value").SetText(str(self.EXPdoubleBonus()))
			self.GetChild("GoldDoubleBonus_Value").SetText(str(self.GoldDoubleBonus()))
			self.GetChild("ItemDoubleBonus_Value").SetText(str(self.ItemDoubleBonus()))
			
	
		except:
			import exception
			exception.Abort("MenuDialog.__LoadWindow.BindObject")


	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()

	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.Hide()

		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Hide()
		return True

	def SetSkillToolTip(self, toolTipSkill):
		self.toolTipSkill = toolTipSkill

	def __OnClickTabButton(self, stateKey):
		self.SetState(stateKey)

	def SetState(self, stateKey):
		
		self.state = stateKey
		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.Hide()

		self.titleBarDict[stateKey].Show()
		

	def GetState(self):
		return self.state

	def RefreshBonus(self):
		if self.isLoaded==0:
			return

		try:
			
			self.GetChild("SwordDef_Value").SetText(str(self.SwordDef()))
			self.GetChild("TwoHandDef_Value").SetText(str(self.TwoHandDef()))
			self.GetChild("DaggerDef_Value").SetText(str(self.DaggerDef()))
			self.GetChild("BellDef_Value").SetText(str(self.BellDef()))
			self.GetChild("FanDef_Value").SetText(str(self.FanDef()))
			self.GetChild("BowDef_Value").SetText(str(self.BowDef()))
			self.GetChild("MagicRes_Value").SetText(str(self.MagicRes()))
			self.GetChild("PointDef_Value").SetText(str(self.PointDef()))
			
			self.GetChild("Block_Value").SetText(str(self.Block()))
			self.GetChild("Dodge_Value").SetText(str(self.Dodge()))			
			self.GetChild("WarriorRes_Value").SetText(str(self.WarriorRes()))
			self.GetChild("NinjaRes_Value").SetText(str(self.NinjaRes()))
			self.GetChild("SuraRes_Value").SetText(str(self.SuraRes()))
			self.GetChild("ShammanRes_Value").SetText(str(self.ShammanRes()))
			self.GetChild("ResToSkillDmg_Value").SetText(str(self.ResToSkillDmg()))
			self.GetChild("AvgDmgRes_Value").SetText(str(self.AvgDmgRes()))
			
			
			self.GetChild("PointAtt_Value").SetText(str(self.PointAtt()))
			self.GetChild("AttHuman_Value").SetText(str(self.AttHuman()))
			self.GetChild("AttAnimals_Value").SetText(str(self.AttAnimals()))
			self.GetChild("AttOrk_Value").SetText(str(self.AttOrk()))
			self.GetChild("AttMilgyo_Value").SetText(str(self.AttMilgyo()))
			self.GetChild("AttUndead_Value").SetText(str(self.AttUndead()))
			self.GetChild("AttDevil_Value").SetText(str(self.AttDevil()))
			self.GetChild("AttMonsters_Value").SetText(str(self.AttMonsters()))
			self.GetChild("Mesi_Value").SetText(str(self.Mesi()))
			self.GetChild("Ikanotitwn_Value").SetText(str(self.Ikanotitwn()))
			self.GetChild("Critical_Value").SetText(str(self.Critical()))
			self.GetChild("Penetrate_Value").SetText(str(self.Penetrate()))
			
			self.GetChild("HPRegen_Value").SetText(str(self.HPRegen()))
			self.GetChild("SPRegen_Value").SetText(str(self.SPRegen()))
			self.GetChild("Poison_Value").SetText(str(self.Poison()))
			self.GetChild("StealHP_Value").SetText(str(self.StealHP()))
			self.GetChild("StealSP_Value").SetText(str(self.StealSP()))
			self.GetChild("AttWarrior_Value").SetText(str(self.AttWarrior()))
			self.GetChild("AttNinja_Value").SetText(str(self.AttNinja()))
			self.GetChild("AttSura_Value").SetText(str(self.AttSura()))
			self.GetChild("AttShaman_Value").SetText(str(self.AttShaman()))
			self.GetChild("EXPdoubleBonus_Value").SetText(str(self.EXPdoubleBonus()))
			self.GetChild("GoldDoubleBonus_Value").SetText(str(self.GoldDoubleBonus()))
			self.GetChild("ItemDoubleBonus_Value").SetText(str(self.ItemDoubleBonus()))
			
	
		except:
			import exception
			exception.Abort("MenuDialog.RefreshBonus.BindObject")
			#pass

		if self.refreshToolTip:
			self.refreshToolTip()
			
	def __LoadRefreshBonus(self):
		self.RefreshBonus()

	def HPRegen(self):
		return player.GetStatus(32)
		
	def SPRegen(self):
		return player.GetStatus(33)
		
	def Poison(self):
		return player.GetStatus(37)

	def Critical(self):
		return player.GetStatus(40)	
		
	def Penetrate(self):
		return player.GetStatus(41)

	def AttHuman(self):
		return player.GetStatus(43)
		
	def AttAnimals(self):
		return player.GetStatus(44)
		
	def AttOrk(self):
		return player.GetStatus(45)
		
	def AttMilgyo(self):
		return player.GetStatus(46)
		
	def AttUndead(self):
		return player.GetStatus(47)
		
	def AttDevil(self):
		return player.GetStatus(48)
		
	def AttMonsters(self):
		return player.GetStatus(53)

	def StealHP(self):
		return player.GetStatus(63)
		
	def StealSP(self):
		return player.GetStatus(64)

	def Block(self):
		return player.GetStatus(67)
		
	def Dodge(self):
		return player.GetStatus(68)

	def SwordDef(self):
		return player.GetStatus(69)
		
	def TwoHandDef(self):
		return player.GetStatus(70)	
		
	def DaggerDef(self):
		return player.GetStatus(71)	
		
	def BellDef(self):
		return player.GetStatus(72)
		
	def FanDef(self):
		return player.GetStatus(73)
		
	def BowDef(self):
		return player.GetStatus(74)	
		
	def MagicRes(self):
		return player.GetStatus(77)	
		
	def PointAtt(self):
		return player.GetStatus(93)	
		
	def PointDef(self):
		return player.GetStatus(132)

	def EXPdoubleBonus(self):
		return player.GetStatus(83)
		
	def GoldDoubleBonus(self):
		return player.GetStatus(84)
		
	def ItemDoubleBonus(self):
		return player.GetStatus(85)

	def AttWarrior(self):
		return player.GetStatus(54)
		
	def AttNinja(self):
		return player.GetStatus(55)
		
	def AttSura(self):
		return player.GetStatus(56)
		
	def AttShaman(self):
		return player.GetStatus(57)

	def Ikanotitwn(self):
		return player.GetStatus(121)
		
	def Mesi(self):
		return player.GetStatus(122)

	def ResToSkillDmg(self):
		return player.GetStatus(123)
	
	def AvgDmgRes(self):
		return player.GetStatus(124)
		
	def WarriorRes(self):
		return player.GetStatus(59)
		
	def NinjaRes(self):
		return player.GetStatus(60)
		
	def SuraRes(self):
		return player.GetStatus(61)
		
	def ShammanRes(self):
		return player.GetStatus(62)
	
	def OnUpdate(self):
		if self.isLoaded == 1:
			self.__LoadRefreshBonus()
