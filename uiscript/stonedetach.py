import uiScriptLocale

WIDTH = 370
HEIGHT = 190
THINBOARD_WIDTH = 250
THINBOARD_HEIGHT = 44
GREEN_COLOR = 0xFFFFC100
PURFLE_COLOR = 0xFF2ECCFA
ROOT_PATH = "d:/ymir work/ui/public/"

window = {
	"name": "GMPanelWindow",

	"x" : SCREEN_WIDTH / 2 - WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - HEIGHT / 2,

	"style": ("movable", "float",),

	"width": WIDTH,
	"height": HEIGHT,

	"children":
	(
		{
			"name": "board",
			"type": "board",
			"style": ("attach",),

			"x": 0,
			"y": 0,

			"width": WIDTH,
			"height": HEIGHT,

			"children":
			(
				## Title
				{
					"name": "TitleBar",
					"type": "titlebar",
					"style": ("attach",),

					"x": 8,
					"y": 6,

					"width": WIDTH - 13,
					"color": "yellow",

					"children":
					(
						{"name": "TitleName", "type": "text", "x": 0, "y": 0, "text": uiScriptLocale.DETACH_STONE_WINDOW, "all_align": "center"},
					),
				},
				{
					"name": "StoneWindow1",
					"type": "window",

					"x": 10,
					"y": 35,
					"width": WIDTH - 20,
					"height": THINBOARD_HEIGHT,
					"children":
					(
						{
							"name": "Metin1Thinboard",
							"type": "thinboard",
							"x": 0,
							"y": 0,
							"width": THINBOARD_WIDTH,
							"height": THINBOARD_HEIGHT,
							"children":
							(
								{
									"name": "MetinImage1",
									"type": "image",
									"x": 4,
									"y": 4,
									"image": "d:/ymir work/ui/game/windows/metin_slot_silver.sub",
									"children":
									(
										{"name": "MetinName1", "type": "text", "x": 40, "y": 9, "text": "", "color": GREEN_COLOR},
										{"name": "MetinNewsName1", "type": "text", "x": 40, "y": 9, "text": "", "color": PURFLE_COLOR},
									),
								},
							),
						},
						{
							"name": "MetinArrow1",
							"type": "image",
							"x": THINBOARD_WIDTH + 10,
							"y": 0,
							"vertical_align": "center",
							"image": "d:/ymir work/ui/game/windows/attach_metin_arrow.sub",
						},
						{
							"name": "MetinButton1",
							"type": "button",

							"x": THINBOARD_WIDTH + 40,
							"y": 0,
							"vertical_align": "center",
							"text": uiScriptLocale.DETACH,

							"default_image": ROOT_PATH + "middle_button_01.sub",
							"over_image": ROOT_PATH + "middle_button_02.sub",
							"down_image": ROOT_PATH + "middle_button_03.sub",
						},
					),
				},
				{
					"name": "StoneWindow2",
					"type": "window",

					"x": 10,
					"y": 85,
					"width": WIDTH - 20,
					"height": THINBOARD_HEIGHT,
					"children":
					(
						{
							"name": "Metin2Thinboard",
							"type": "thinboard",
							"x": 0,
							"y": 0,
							"width": THINBOARD_WIDTH,
							"height": THINBOARD_HEIGHT,
							"children":
							(
								{
									"name": "MetinImage2",
									"type": "image",
									"x": 4,
									"y": 4,
									"image": "d:/ymir work/ui/game/windows/metin_slot_silver.sub",
									"children":
									(
										{"name": "MetinName2", "type": "text", "x": 40, "y": 9, "text": "", "color": GREEN_COLOR},
										{"name": "MetinNewsName2", "type": "text", "x": 40, "y": 9, "text": "", "color": PURFLE_COLOR},
									),
								},
							),
						},
						{
							"name": "MetinArrow2",
							"type": "image",
							"x": THINBOARD_WIDTH + 10,
							"y": 0,
							"vertical_align": "center",
							"image": "d:/ymir work/ui/game/windows/attach_metin_arrow.sub",
						},
						{
							"name": "MetinButton2",
							"type": "button",

							"x": THINBOARD_WIDTH + 40,
							"y": 0,
							"vertical_align": "center",
							"text": uiScriptLocale.DETACH,

							"default_image": ROOT_PATH + "middle_button_01.sub",
							"over_image": ROOT_PATH + "middle_button_02.sub",
							"down_image": ROOT_PATH + "middle_button_03.sub",
						},
					),
				},
				{
					"name": "StoneWindow3",
					"type": "window",

					"x": 10,
					"y": 135,
					"width": WIDTH - 20,
					"height": THINBOARD_HEIGHT,
					"children":
					(
						{
							"name": "Metin3Thinboard",
							"type": "thinboard",
							"x": 0,
							"y": 0,
							"width": THINBOARD_WIDTH,
							"height": THINBOARD_HEIGHT,
							"children":
							(
								{
									"name": "MetinImage3",
									"type": "image",
									"x": 4,
									"y": 4,
									"image": "d:/ymir work/ui/game/windows/metin_slot_silver.sub",
									"children":
									(
										{"name": "MetinName3", "type": "text", "x": 40, "y": 9, "text": "", "color": GREEN_COLOR},
										{"name": "MetinNewsName3", "type": "text", "x": 40, "y": 9, "text": "", "color": PURFLE_COLOR},
									),
								},
							),
						},
						{
							"name": "MetinArrow3",
							"type": "image",
							"x": THINBOARD_WIDTH + 10,
							"y": 0,
							"vertical_align": "center",
							"image": "d:/ymir work/ui/game/windows/attach_metin_arrow.sub",
						},
						{
							"name": "MetinButton3",
							"type": "button",

							"x": THINBOARD_WIDTH + 40,
							"y": 0,
							"vertical_align": "center",
							"text": uiScriptLocale.DETACH,

							"default_image": ROOT_PATH + "middle_button_01.sub",
							"over_image": ROOT_PATH + "middle_button_02.sub",
							"down_image": ROOT_PATH + "middle_button_03.sub",
						},
					),
				},
			),
		},
	),
}
