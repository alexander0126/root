import ui
import snd
import systemSetting
import net
import chat
import app
import localeinfo
import constInfo
import chrmgr
import player
import musicInfo
import uiSelectMusic
import background

if app.ENABLE_CAMERA_FOVE:
	FOV_LEVEL_MAX_NUM = 5

blockMode = 0
class OptionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE SYSTEM OPTION DIALOG"

	def __Initialize(self):
		self.tilingMode = 0
		self.titleBar = 0
		self.changeMusicButton = 0
		self.selectMusicFile = 0
		self.ctrlMusicVolume = 0
		self.ctrlSoundVolume = 0
		self.musicListDlg = 0
		self.tilingApplyButton = 0
		self.cameraModeButtonList = []
		self.fogModeButtonList = []
		self.tilingModeButtonList = []
		self.ctrlShadowQuality = 0
		if app.__BL_FOG_FIX__:
			self.fogButtonList	= []
		if app.STONE_SCALE_SYSTEM:
			self.ctrlStoneScale = 0
		if app.ENABLE_CAMERA_FOVE:
			self.fovlevel = 0
			self.fovlevelapplybutton = 0
			self.fovlevelbuttonlist = []
		
	def Destroy(self):
		self.ClearDictionary()
		self.__Initialize()
		print " -------------------------------------- DESTROY SYSTEM OPTION DIALOG"

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("System.OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.selectMusicFile = GetObject("bgm_file")
			self.changeMusicButton = GetObject("bgm_button")
			self.ctrlMusicVolume = GetObject("music_volume_controller")
			self.ctrlSoundVolume = GetObject("sound_volume_controller")			
			self.cameraModeButtonList.append(GetObject("camera_short"))
			self.cameraModeButtonList.append(GetObject("camera_long"))
			if app.__BL_FOG_FIX__:
				self.fogButtonList.append(GetObject("fog_off"))
				self.fogButtonList.append(GetObject("fog_on"))
			else:
				self.fogModeButtonList.append(GetObject("fog_level0"))
				self.fogModeButtonList.append(GetObject("fog_level1"))
				self.fogModeButtonList.append(GetObject("fog_level2"))
			if app.STONE_SCALE_SYSTEM:
				self.ctrlStoneScale = GetObject("stone_scale_controller")
			if app.ENABLE_CAMERA_FOVE:
				for i in xrange(1, FOV_LEVEL_MAX_NUM + 1):
					self.fovlevelbuttonlist.append(GetObject("FOV_TYPE%d" % i))
				self.fovlevelapplybutton = GetObject("fovlevel_apply")
			self.tilingModeButtonList.append(GetObject("tiling_cpu"))
			self.tilingModeButtonList.append(GetObject("tiling_gpu"))
			self.tilingApplyButton=GetObject("tiling_apply")
		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/systemoptiondialog.py")
		self.__Load_BindObject()

		self.SetCenterPosition()
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.ctrlMusicVolume.SetSliderPos(float(systemSetting.GetMusicVolume()))
		self.ctrlMusicVolume.SetEvent(ui.__mem_func__(self.OnChangeMusicVolume))

		self.ctrlSoundVolume.SetSliderPos(float(systemSetting.GetSoundVolume()) / 5.0)
		self.ctrlSoundVolume.SetEvent(ui.__mem_func__(self.OnChangeSoundVolume))
		self.changeMusicButton.SAFE_SetEvent(self.__OnClickChangeMusicButton)

		self.cameraModeButtonList[0].SAFE_SetEvent(self.__OnClickCameraModeShortButton)
		self.cameraModeButtonList[1].SAFE_SetEvent(self.__OnClickCameraModeLongButton)

		if app.__BL_FOG_FIX__:
			self.fogButtonList[0].SAFE_SetEvent(self.__OnClickFogModeOffButton)
			self.fogButtonList[1].SAFE_SetEvent(self.__OnClickFogModeOnButton)
		else:
			self.fogModeButtonList[0].SAFE_SetEvent(self.__OnClickFogModeLevel0Button)
			self.fogModeButtonList[1].SAFE_SetEvent(self.__OnClickFogModeLevel1Button)
			self.fogModeButtonList[2].SAFE_SetEvent(self.__OnClickFogModeLevel2Button)

		if app.STONE_SCALE_SYSTEM:
			self.ctrlStoneScale.SetSliderPos(float(systemSetting.GetStoneScale()))
			self.ctrlStoneScale.SetEvent(ui.__mem_func__(self.OnChangeStoneScale))

		self.tilingModeButtonList[0].SAFE_SetEvent(self.__OnClickTilingModeCPUButton)
		self.tilingModeButtonList[1].SAFE_SetEvent(self.__OnClickTilingModeGPUButton)

		self.tilingApplyButton.SAFE_SetEvent(self.__OnClickTilingApplyButton)

		self.__SetCurTilingMode()

		self.__ClickRadioButton(self.fogModeButtonList, constInfo.GET_FOG_LEVEL_INDEX())
		self.__ClickRadioButton(self.cameraModeButtonList, constInfo.GET_CAMERA_MAX_DISTANCE_INDEX())

		if app.__BL_FOG_FIX__:
			self.__ClickRadioButton(self.fogButtonList, background.GetFogMode())

		if app.ENABLE_CAMERA_FOVE:
			self.__ClickRadioButton(self.fovlevelbuttonlist,systemSetting.GetFovValue())

		if musicInfo.fieldMusic==musicInfo.METIN2THEMA:
			self.selectMusicFile.SetText(uiSelectMusic.DEFAULT_THEMA)
		else:
			self.selectMusicFile.SetText(musicInfo.fieldMusic[:25])

		if app.ENABLE_CAMERA_FOVE:
			for i in xrange(FOV_LEVEL_MAX_NUM):
				self.fovlevelbuttonlist[i].SAFE_SetEvent(self.__OnClickFovButton, i)
			self.fovlevelapplybutton.SAFE_SetEvent(self.__OnClickFovApplyButton)

	def __OnClickTilingModeCPUButton(self):
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_CPU_TILING_1)
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_CPU_TILING_2)
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_CPU_TILING_3)
		self.__SetTilingMode(0)

	def __OnClickTilingModeGPUButton(self):
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_GPU_TILING_1)
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_GPU_TILING_2)
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_GPU_TILING_3)
		self.__SetTilingMode(1)

	def __OnClickTilingApplyButton(self):
		self.__NotifyChatLine(localeinfo.SYSTEM_OPTION_TILING_EXIT)
		if 0==self.tilingMode:
			background.EnableSoftwareTiling(1)
		else:
			background.EnableSoftwareTiling(0)

		net.ExitGame()

	def __OnClickChangeMusicButton(self):
		if not self.musicListDlg:
			
			self.musicListDlg=uiSelectMusic.FileListDialog()
			self.musicListDlg.SAFE_SetSelectEvent(self.__OnChangeMusic)

		self.musicListDlg.Open()

		
	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()


	def __SetTilingMode(self, index):
		self.__ClickRadioButton(self.tilingModeButtonList, index)
		self.tilingMode=index

	def __SetCameraMode(self, index):
		constInfo.SET_CAMERA_MAX_DISTANCE_INDEX(index)
		self.__ClickRadioButton(self.cameraModeButtonList, index)

	def __SetFogLevel(self, index):
		constInfo.SET_FOG_LEVEL_INDEX(index)
		self.__ClickRadioButton(self.fogModeButtonList, index)

	def __OnClickCameraModeShortButton(self):
		self.__SetCameraMode(0)

	def __OnClickCameraModeLongButton(self):
		self.__SetCameraMode(1)

	def __OnClickFogModeLevel0Button(self):
		self.__SetFogLevel(0)

	def __OnClickFogModeLevel1Button(self):
		self.__SetFogLevel(1)

	def __OnClickFogModeLevel2Button(self):
		self.__SetFogLevel(2)

	if app.__BL_FOG_FIX__:
		def __OnClickFogModeOnButton(self):
			background.SetFogMode(True)
			self.__ClickRadioButton(self.fogButtonList, 1)
		def __OnClickFogModeOffButton(self):
			background.SetFogMode(False)
			self.__ClickRadioButton(self.fogButtonList, 0)

	if app.STONE_SCALE_SYSTEM:
		def OnChangeStoneScale(self):
			pos = self.ctrlStoneScale.GetSliderPos()
			systemSetting.SetStoneScale(pos)

	if app.ENABLE_CAMERA_FOVE:
		def __OnClickFovButton(self, index):
			self.__ClickRadioButton(self.fovlevelbuttonlist, index)
			self.fovlevel = index
		def __OnClickFovApplyButton(self):
			systemSetting.SetFovValue(self.fovlevel)

	def __OnChangeMusic(self, fileName):
		self.selectMusicFile.SetText(fileName[:25])

		if musicInfo.fieldMusic != "":
			snd.FadeOutMusic("miles/BGM/"+ musicInfo.fieldMusic)

		if fileName==uiSelectMusic.DEFAULT_THEMA:
			musicInfo.fieldMusic=musicInfo.METIN2THEMA
		else:
			musicInfo.fieldMusic=fileName

		musicInfo.SaveLastPlayFieldMusic()
		
		if musicInfo.fieldMusic != "":
			snd.FadeInMusic("miles/BGM/" + musicInfo.fieldMusic)

	def OnChangeMusicVolume(self):
		pos = self.ctrlMusicVolume.GetSliderPos()
		snd.SetMusicVolume(pos * net.GetFieldMusicVolume())
		systemSetting.SetMusicVolume(pos)

	def OnChangeSoundVolume(self):
		pos = self.ctrlSoundVolume.GetSliderPos()
		snd.SetSoundVolumef(pos)
		systemSetting.SetSoundVolumef(pos)

	def OnChangeShadowQuality(self):
		pos = self.ctrlShadowQuality.GetSliderPos()
		systemSetting.SetShadowLevel(int(pos / 0.2))

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.__SetCurTilingMode()
		self.Hide()

	def __SetCurTilingMode(self):
		if background.IsSoftwareTiling():
			self.__SetTilingMode(0)
		else:
			self.__SetTilingMode(1)	

	def __NotifyChatLine(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, text)

