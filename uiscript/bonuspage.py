import uiScriptLocale

MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"

window = {
	"name" : "bonuspage",
	"style" : ("movable", "float",),

	"x" : 100,
	"y" : 100,

	"width" : 390,
	"height" : 655,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 390,
			"height" : 655,

			"children" :
			(
				{
					"name" : "Bonus_TitleBar",
					"type" : "titlebar",
					#"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 375,
					"color" : "red",

					"children" :
					(
						{ 
						"name":"TitleName", 
						"type":"text", 
						
						"x":0, 
						"y":-1, 
						
						"text":"Καρτέλα Bonus", 
						"all_align":"center" 
						},
					),
				},
				## Page Area
				{
					"name" : "Bonus_Page",
					"type" : "window",
					#"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 390,
					"height" : 690,

					"children" :
					(
						## Barra
						{ "name":"Bonus_Bar_Difese", "type":"horizontalbar", "x":12, "y":11, "width":363, },
						{ "name":"Bonus_Bar_Text_Difese", "type":"text", "x":15, "y":13, "text":"Αμυντικά Bonus", "r":1.0, "g":0.8, "b":0.0, "a":1.0 },

						#SwordDef
						{ "name":"SwordDef", "type":"text", "x":15, "y":35, "text":"’μυνα Ξίφους:" },
						{
							"name":"SwordDef", "type":"window", "x":132, "y":35, "width":45, "height":20, 
							"children" :
							(
								{ "name":"SwordDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"SwordDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#TwoHandDef
						{ "name":"TwoHandDef", "type":"text", "x":15, "y":60, "text":"’μυνα 2 Χεριών:" },
						{
							"name":"TwoHandDef", "type":"window", "x":132, "y":60, "width":45, "height":20, 
							"children" :
							(
								{ "name":"TwoHandDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"TwoHandDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#DaggerDef
						{ "name":"DaggerDef", "type":"text", "x":15, "y":85, "text":"’μυνα Στιλέτου:" },
						{
							"name":"DaggerDef", "type":"window", "x":132, "y":85, "width":45, "height":20, 
							"children" :
							(
								{ "name":"DaggerDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"DaggerDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#BellDef
						{ "name":"BellDef", "type":"text", "x":15, "y":110, "text":"’μυνα Καμπάνας:" },
						{
							"name":"BellDef", "type":"window", "x":132, "y":110, "width":45, "height":20, 
							"children" :
							(
								{ "name":"BellDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"BellDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#FanDef
						{ "name":"FanDef", "type":"text", "x":15, "y":135, "text":"’μυνα Βεντάλιας:" },
						{
							"name":"FanDef", "type":"window", "x":132, "y":135, "width":45, "height":20, 
							"children" :
							(
								{ "name":"FanDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"FanDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#BowDef
						{ "name":"BowDef", "type":"text", "x":15, "y":160, "text":"Αντίσταση Βέλους:" },
						{
							"name":"BowDef", "type":"window", "x":132, "y":160, "width":45, "height":20, 
							"children" :
							(
								{ "name":"BowDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"BowDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#MagicRes
						{ "name":"MagicRes", "type":"text", "x":15, "y":185, "text":"Μαγική Αντίσταση:" },
						{
							"name":"MagicRes", "type":"window", "x":132, "y":185, "width":45, "height":20, 
							"children" :
							(
								{ "name":"MagicRes_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"MagicRes_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#PointDef
						{ "name":"PointDef", "type":"text", "x":15, "y":210, "text":"Μείωση hit %:" },
						{
							"name":"PointDef", "type":"window", "x":132, "y":210, "width":45, "height":20, 
							"children" :
							(
								{ "name":"PointDef_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"PointDef_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						#------------------------------------------------------------------------------------------------------------------------
						#Block
						{ "name":"Block", "type":"text", "x":195, "y":35, "text":"Πιθ. Απόκρουσης:" },
						{
							"name":"Block", "type":"window", "x":325, "y":35, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Block_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Block_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#Dodge
						{ "name":"Dodge", "type":"text", "x":195, "y":60, "text":"Αποφυγή Βελών:" },
						{
							"name":"Dodge", "type":"window", "x":325, "y":60, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Dodge_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Dodge_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#WarriorRes
						{ "name":"WarriorRes", "type":"text", "x":195, "y":85, "text":"’μυνα Πολεμιστή:" },
						{
							"name":"WarriorRes", "type":"window", "x":325, "y":85, "width":45, "height":20, 
							"children" :
							(
								{ "name":"WarriorRes_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"WarriorRes_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#NinjaRes
						{ "name":"NinjaRes", "type":"text", "x":195, "y":110, "text":"’μυνα Ninja:" },
						{
							"name":"NinjaRes", "type":"window", "x":325, "y":110, "width":45, "height":20, 
							"children" :
							(
								{ "name":"NinjaRes_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"NinjaRes_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#SuraRes
						{ "name":"SuraRes", "type":"text", "x":195, "y":135, "text":"’μυνα Sura:" },
						{
							"name":"SuraRes", "type":"window", "x":325, "y":135, "width":45, "height":20, 
							"children" :
							(
								{ "name":"SuraRes_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"SuraRes_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#ShammanRes
						{ "name":"ShammanRes", "type":"text", "x":195, "y":160, "text":"’μυνα Σαμάνου:" },
						{
							"name":"ShammanRes", "type":"window", "x":325, "y":160, "width":45, "height":20, 
							"children" :
							(
								{ "name":"ShammanRes_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"ShammanRes_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#ResToSkillDmg
						{ "name":"ResToSkillDmg", "type":"text", "x":195, "y":185, "text":"Αντίστ. Ικανότητας:" },
						{
							"name":"ResToSkillDmg", "type":"window", "x":325, "y":185, "width":45, "height":20, 
							"children" :
							(
								{ "name":"ResToSkillDmg_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"ResToSkillDmg_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AvgDmgRes
						{ "name":"AvgDmgRes", "type":"text", "x":195, "y":210, "text":"Μέση αντ. Ζημιάς:" },
						{
							"name":"AvgDmgRes", "type":"window", "x":325, "y":210, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AvgDmgRes_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AvgDmgRes_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},

						
						
						############ ΕΠΙΘΕΤΙΚΑ BONUS
						{ "name":"Reaction_Bar", "type":"horizontalbar", "x":12, "y":235, "width":363, },
						{ "name":"Reaction_Bar_Text", "type":"text", "x":15, "y":235, "text":"Επιθετικά Bonus", "r":1.0, "g":0.8, "b":0.0, "a":1.0 },

						#PointAtt
						{ "name":"PointAtt", "type":"text", "x":15, "y":255, "text":"Αξία Επίθεσης %:" },
						{
							"name":"PointAtt", "type":"window", "x":132, "y":255, "width":45, "height":20, 
							"children" :
							(
								{ "name":"PointAtt_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"PointAtt_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttHuman
						{ "name":"AttHuman", "type":"text", "x":15, "y":280, "text":"Ημιάνθρωποι:" },
						{
							"name":"AttHuman", "type":"window", "x":132, "y":280, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttHuman_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttHuman_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttAnimals
						{ "name":"AttAnimals", "type":"text", "x":15, "y":305, "text":"Δυνατό σε Ζώα:" },
						{
							"name":"AttAnimals", "type":"window", "x":132, "y":305, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttAnimals_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttAnimals_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttOrk
						{ "name":"AttOrk", "type":"text", "x":15, "y":330, "text":"Δυνατό σε Ορκ:" },
						{
							"name":"AttOrk", "type":"window", "x":132, "y":330, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttOrk_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttOrk_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttMilgyo
						{ "name":"AttMilgyo", "type":"text", "x":15, "y":355, "text":"Δυν. σε Εσωτερικούς:" },
						{
							"name":"AttMilgyo", "type":"window", "x":132, "y":355, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttMilgyo_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttMilgyo_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttUndead
						{ "name":"AttUndead", "type":"text", "x":15, "y":380, "text":"Δυν. σε Απέθαντους:" },
						{
							"name":"AttUndead", "type":"window", "x":132, "y":380, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttUndead_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttUndead_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttDevil
						{ "name":"AttDevil", "type":"text", "x":15, "y":405, "text":"Δυνατό σε Διάβολο:" },
						{
							"name":"AttDevil", "type":"window", "x":132, "y":405, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttDevil_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttDevil_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttMonsters
						{ "name":"AttMonsters", "type":"text", "x":15, "y":430, "text":"Δυνατό σε Τέρατα:" },
						{
							"name":"AttMonsters", "type":"window", "x":132, "y":430, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttMonsters_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttMonsters_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#Mesi
						{ "name":"Mesi", "type":"text", "x":15, "y":455, "text":"Μέση Ζημιά:" },
						{
							"name":"Mesi", "type":"window", "x":132, "y":455, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Mesi_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Mesi_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#Ikanotitwn
						{ "name":"Ikanotitwn", "type":"text", "x":15, "y":480, "text":"Ικανοτήτων:" },
						{
							"name":"Ikanotitwn", "type":"window", "x":132, "y":480, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Ikanotitwn_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Ikanotitwn_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#Critical
						{ "name":"Critical", "type":"text", "x":15, "y":505, "text":"Κρίσιμο:" },
						{
							"name":"Critical", "type":"window", "x":132, "y":505, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Critical_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Critical_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#Penetrate
						{ "name":"Penetrate", "type":"text", "x":15, "y":530, "text":"Διάτρηση:" },
						{
							"name":"Penetrate", "type":"window", "x":132, "y":530, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Penetrate_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Penetrate_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						#------------------------------------------------------------------------------------------------------------------------
						#HPRegen
						{ "name":"HPRegen", "type":"text", "x":195, "y":255, "text":"Αναγέννηση HP:" },
						{
							"name":"HPRegen", "type":"window", "x":325, "y":255, "width":45, "height":20, 
							"children" :
							(
								{ "name":"HPRegen_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"HPRegen_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#SPRegen
						{ "name":"SPRegen", "type":"text", "x":195, "y":280, "text":"Αναγέννηση SP:" },
						{
							"name":"SPRegen", "type":"window", "x":325, "y":280, "width":45, "height":20, 
							"children" :
							(
								{ "name":"SPRegen_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"SPRegen_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#Poison
						{ "name":"Poison", "type":"text", "x":195, "y":305, "text":"Δηλητηρίαση:" },
						{
							"name":"Poison", "type":"window", "x":325, "y":305, "width":45, "height":20, 
							"children" :
							(
								{ "name":"Poison_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"Poison_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#StealHP
						{ "name":"StealHP", "type":"text", "x":195, "y":330, "text":"Απορρόφηση HP:" },
						{
							"name":"StealHP", "type":"window", "x":325, "y":330, "width":45, "height":20, 
							"children" :
							(
								{ "name":"StealHP_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"StealHP_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#StealSP
						{ "name":"StealSP", "type":"text", "x":195, "y":355, "text":"Απορρόφηση SP:" },
						{
							"name":"StealSP", "type":"window", "x":325, "y":355, "width":45, "height":20, 
							"children" :
							(
								{ "name":"StealSP_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"StealSP_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttWarrior
						{ "name":"AttWarrior", "type":"text", "x":195, "y":380, "text":"Δυν. σε Πολεμιστές:" },
						{
							"name":"AttWarrior", "type":"window", "x":325, "y":380, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttWarrior_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttWarrior_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						#AttNinja
						{ "name":"AttNinja", "type":"text", "x":195, "y":405, "text":"Δυνατό σε Ninja:" },
						{
							"name":"AttNinja", "type":"window", "x":325, "y":405, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttNinja_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttNinja_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#AttSura
						{ "name":"AttSura", "type":"text", "x":195, "y":430, "text":"Δυνατό σε Sura:" },
						{
							"name":"AttSura", "type":"window", "x":325, "y":430, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttSura_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttSura_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						#AttShaman
						{ "name":"AttShaman", "type":"text", "x":195, "y":455, "text":"Δυνατό σε Σαμάνους:" },
						{
							"name":"AttShaman", "type":"window", "x":325, "y":455, "width":45, "height":20, 
							"children" :
							(
								{ "name":"AttShaman_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"AttShaman_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						#EXPdoubleBonus
						{ "name":"EXPdoubleBonus", "type":"text", "x":195, "y":480, "text":"Πιθ. για EXP Bonus:" },
						{
							"name":"EXPdoubleBonus", "type":"window", "x":325, "y":480, "width":45, "height":20, 
							"children" :
							(
								{ "name":"EXPdoubleBonus_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"EXPdoubleBonus_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#GoldDoubleBonus
						{ "name":"GoldDoubleBonus", "type":"text", "x":195, "y":505, "text":"Πιθ. για 2πλάσια yang:" },
						{
							"name":"GoldDoubleBonus", "type":"window", "x":325, "y":505, "width":45, "height":20, 
							"children" :
							(
								{ "name":"GoldDoubleBonus_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"GoldDoubleBonus_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						#ItemDoubleBonus
						{ "name":"ItemDoubleBonus", "type":"text", "x":195, "y":530, "text":"Πιθ. για 2πλάσια αντικ.:" },
						{
							"name":"ItemDoubleBonus", "type":"window", "x":325, "y":530, "width":45, "height":20, 
							"children" :
							(
								{ "name":"ItemDoubleBonus_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
								{ "name":"ItemDoubleBonus_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							)
						},
						
						{ "name":"Info_Bar", "type":"horizontalbar", "x":13, "y":565, "width":363, },
						{ "name":"Info_Bar_Text", "type":"text", "x":18, "y":565, "text":"Όλα τα bonus αναφέρονται σε ποσοστό επί τοις εκατό. Η μείωση", "r":0.75, "g":0.85, "b":0.90, "a":1.0 },
						{ "name":"Info_Bar2", "type":"horizontalbar", "x":13, "y":581, "width":363, },
						{ "name":"Info_Bar_Text2", "type":"text", "x":18, "y":580, "text":"ζημιάς του Φόβου και της Ευλογίας, όπως και η απορρόφηση HP", "r":0.75, "g":0.85, "b":0.90, "a":1.0 },
						{ "name":"Info_Bar3", "type":"horizontalbar", "x":13, "y":596, "width":363, },
						{ "name":"Info_Bar_Text3", "type":"text", "x":18, "y":596, "text":"της Επάρατης Λεπίδας, δεν αναγράφονται.", "r":0.7, "g":0.8, "b":0.9, "a":1.0 },
						
					),
				},
			),
		},
	),
}
