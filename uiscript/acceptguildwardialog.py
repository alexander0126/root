import uiScriptLocale

window = {
	"name" : "InputDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 230,
	"height" : 215, # default: 130

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 230,
			"height" : 215, # default: 130

			"title" : uiScriptLocale.GUILD_WAR_ACCEPT,

			"children" :
			(
			# if app.ENABLE_IMPROVED_GUILD_WAR_SYSTEM:
				{
					"name" : "InputSlotScore",
					"type" : "slotbar",

					"x" : 50,
					"y" : 97,

					"width" : 130,
					"height" : 18,

					"children" :
					(
						{
							"name" : "InputValueScore",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},
				{
					"name" : "InputSlotUser",
					"type" : "slotbar",

					"x" : 50,
					"y" : 127,

					"width" : 130,
					"height" : 18,

					"children" :
					(
						{
							"name" : "InputValueUser",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},
				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : 50,
					"y" : 37,
					"width" : 130,
					"height" : 18,

					"children" :
					(
						{
							"name" : "InputValue",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

						},
					),
				},
				## Input Slot
				{
					"name" : "GameType", "x" : -16, "y" : 65, "width" : 65+45*4, "height" : 20,

					"children" :
					(
						{
							"name" : "NormalButton",
							"type" : "radio_button",

							"x" : 65,
							"y" : 0,

							"text" : uiScriptLocale.GUILD_WAR_NORMAL,

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
						{
							"name" : "WarpButton",
							"type" : "radio_button",

							"x" : 65+45*1,
							"y" : 0,

							"text" : uiScriptLocale.GUILD_WAR_WARP,

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
						{
							"name" : "CTFButton",
							"type" : "radio_button",

							"x" : 65+45*2,
							"y" : 0,

							"text" : uiScriptLocale.GUILD_WAR_CTF,

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
					),
				},
				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 165, # default: 95
					"horizontal_align" : "center",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 5 + 30,
					"y" : 165, # default: 95
					"horizontal_align" : "center",

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}
