window = {
	"name" : "CreateCharacterWindow",
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,	"height" : SCREEN_HEIGHT,
	"children" : (
		{
			"name" : "BackGround",
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1366.0,
			"y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "sistimata/interface/characterwindow/background.tga",
			"children" : (
				{
					"name" : "board_main",
					"type" : "window",
					"x" : -300, "y" : 20,
					"width" : 352, "height" : 457,
					"vertical_align" : "center",
					"horizontal_align" : "center",
					"children" :(
						{
							"name" : "board",
							"type" : "image",
							"x" : 0, "y" : 0,
							"image" : "sistimata/interface/characterwindow/create/board.tga",
							"children" : (
								{
									"name" : "name_slotbar",
									"type" : "image",
									"x" : 35, "y" : 135,
									"horizontal_align" : "center",
									"vertical_align" : "center",
									"image" : "sistimata/interface/characterwindow/select/slotbar.tga",
									"children" : (
										{
											"name" : "name",
											"type" : "editline",
											"x" : 12, "y" : 10,
											"width" : 200, "height" : 16,
											"color" : 0xffc8aa80,
											"input_limit": 16,
											"enable_codepage": 0,
										},
									),
								},
								{
									"name" : "char1",
									"type" : "radio_button",
									"x" : -70, "y" : -85,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/warrior_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/warrior_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/warrior_2.tga",
								},
								{
									"name" : "char2",
									"type" : "radio_button",
									"x" : 70, "y" : -85,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/assassin_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/assassin_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/assassin_2.tga",
								},
								{
									"name" : "char3",
									"type" : "radio_button",
									"x" : -70, "y" : -20,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/sura_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/sura_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/sura_2.tga",
								},
								{
									"name" : "char4",
									"type" : "radio_button",
									"x" : 70, "y" : -20,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/shaman_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/shaman_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/shaman_2.tga",
								},
								{
									"name" : "shape1",
									"type" : "radio_button",
									"x" : -70, "y" : 30,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/shape1_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/shape1_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/shape1_2.tga",
								},
								{
									"name" : "shape2",
									"type" : "radio_button",
									"x" : 70, "y" : 30,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/shape2_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/shape2_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/shape2_2.tga",
								},
								{
									"name" : "gender_man",
									"type" : "radio_button",
									"x" : -70, "y" : 80,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/man_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/man_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/man_2.tga",
								},
								{
									"name" : "gender_woman",
									"type" : "radio_button",
									"x" : 70, "y" : 80,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/woman_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/woman_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/woman_2.tga",
								},
								{
									"name" : "create_button",
									"type" : "button",
									"x" : 0, "y" : 175,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "sistimata/interface/characterwindow/create/create_0.tga",
									"over_image" : "sistimata/interface/characterwindow/create/create_1.tga",
									"down_image" : "sistimata/interface/characterwindow/create/create_2.tga",
								},
							),
						},
					),
				},
				{
					"name" : "exit_button",
					"type" : "button",
					"x" : SCREEN_WIDTH - 115, "y" : 10,
					"default_image" : "sistimata/interface/loginwindow/exit_0.tga",
					"over_image" :  "sistimata/interface/loginwindow/exit_1.tga",
					"down_image" : "sistimata/interface/loginwindow/exit_2.tga",
				},
			),
		},
	),
}
