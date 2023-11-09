import ui
import app
import grp
import time
import chat
import item
import systemSetting
import playerSettingModule
import dbg

FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
	playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
	playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
	playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
	playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
	playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
	playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
	playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
}

DROP_MESSAGE_TIME = 4
DROP_MAX_STACK = 13

class MessageObject(ui.Bar):
	def __init__(self):
		ui.Bar.__init__(self)

		self.__killWeapon = None

		self.__killerName = None
		self.__killerRace = None

		self.__victimName = None
		self.__victimRace = None

		self.endTime = time.clock() + DROP_MESSAGE_TIME

		self.SetSize(250, 25)
		self.SetColor(0x77000000)

	def __del__(self):
		ui.Bar.__del__(self)


	def SetKillWeapon(self, weaponVnum):
		item.SelectItem(weaponVnum)

		self.__killWeapon = ui.ExpandedImageBox()
		self.__killWeapon.SetParent(self)		
		try:
			self.__killWeapon.LoadImage(item.GetIconImageFileName())
		except:
			self.__killWeapon.Hide()
		self.__killWeapon.SetPosition(0, 35)
		self.__killWeapon.SetScale(0.3, 0.3)

	def SetKillerInfo(self, killerName, killerRace):
		self.__killerName = ui.TextLine()
		self.__killerName.SetParent(self)
		self.__killerName.SetPosition(25, 3)
		self.__killerName.SetText(killerName)
		self.__killerName.SetOutline()
		self.__killerName.SetFeather(False)
		self.__killerName.SetPackedFontColor(0xff00e5ee)


		self.__killerRace = ui.ExpandedImageBox()
		self.__killerRace.SetParent(self)		
		try:
			self.__killerRace.LoadImage(FACE_IMAGE_DICT[int(killerRace)])
		except:
			self.__killerRace.Hide()
		self.__killerRace.SetPosition(0, 5)
		self.__killerRace.SetScale(0.3, 0.3)
		
	def SetVictimInfo(self, victimName, victimRace):
		self.__victimName = ui.TextLine()
		self.__victimName.SetParent(self)
		self.__victimName.SetPosition(155, 3)
		self.__victimName.SetText(victimName)
		self.__victimName.SetOutline()
		self.__victimName.SetFeather(False)
		self.__victimName.SetPackedFontColor(0xffff0000)


		self.__victimRace = ui.ExpandedImageBox()
		self.__victimRace.SetParent(self)		
		try:
			self.__victimRace.LoadImage(FACE_IMAGE_DICT[int(victimRace)])
		except:
			self.__victimRace.Hide()
		self.__victimRace.SetPosition(135, 5)
		self.__victimRace.SetScale(0.3, 0.3)

	def ShowInfos(self):
		self.__killerName.Show()
		self.__killerRace.Show()

		self.__victimName.Show()
		self.__victimRace.Show()

		#self.__killWeaponVnum.Show()

	def isTimeout(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			return True
		return False


class MessageQueue(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)

		self.stack = []

		self.lastClock = 0
		self.timeDiff = 0.5
		self.nextY = 0

		self.__Reset()

	def __del__(self):
		ui.Window.__del__(self)

		self.stack = None

	def OnMessage(self, killerName, killerRace, victimName, victimRace, killWeaponVnum = 0):
		message = MessageObject()

		message.SetParent(self)
		#if killWeaponVnum:
		#	message.SetKillWeapon(killWeaponVnum)
		message.SetKillerInfo(killerName, killerRace)
		message.SetVictimInfo(victimName, victimRace)

		message.Hide()

		count = len(self.stack)

		if count == DROP_MAX_STACK:
			self.stack.remove(self.stack[0])

		self.stack.append(message)
		self.__Render()

	def __Reset(self):
		#self.SetSize(250, 426)
		self.SetPosition(systemSetting.GetWidth()- 250, -200)

		self.Show()

	def __Render(self):
		for it in self.stack:
			if it.isTimeout():
				self.stack.remove(it)

		stack = list(self.stack)
		stack.reverse()

		self.nextY = 408

		for it in stack:
			it.SetPosition(0, self.nextY)

			if not it.IsShow():
				it.Show()
				it.ShowInfos()

			self.nextY += 27

	def OnUpdate(self):
		if len(self.stack) > 0:
			if (app.GetTime() - self.lastClock) >= self.timeDiff:
				self.lastClock = app.GetTime()
				self.__Render()
