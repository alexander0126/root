import uiScriptLocale
import item

EQUIPMENT_START_INDEX = 180
window = {
	"name" : "InventoryWindow",
	"x" : SCREEN_WIDTH - 376,
	"y" : SCREEN_HEIGHT - 37 - 605,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 605,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 605,

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 161,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "Equipment_Base",
					"type" : "expanded_image",

					"x" : 10,
					"y" : 33,

					"image" : "d:/ymir work/ui/game/windows/equipment_base.sub",

					"children" :
					(

						{
							"name" : "EquipmentSlot",
							"type" : "slot",

							"x" : 3,
							"y" : 3,

							"width" : 150,
							"height" : 182,

							"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64},
										{"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+2, "x":39, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
										{"index":EQUIPMENT_START_INDEX+5, "x":114, "y":84, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+6, "x":114, "y":52, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+7, "x":2, "y":113, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+8, "x":75, "y":113, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32},
										{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
									),
						},

						{
							"name" : "DSSButton",
							"type" : "button",

							"x" : 114,
							"y" : 120,

							"tooltip_text" : uiScriptLocale.LOCKED_BUTTON_INVENTORYY,

							"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_01.tga",
							"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_02.tga",
							"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_03.tga",
						},
						##if app.FIX_BUFF_TROLL:
						{
							"name" : "FixBuffShamy",
							"type" : "button",
							"x" : 114,
							"y" : 153,
							"tooltip_text" : uiScriptLocale.DISABLE_BUFF_SHAMY,
							"default_image" : "d:/ymir work/ui/game/TaskBar/anti_exp_01.tga",
							"over_image" : "d:/ymir work/ui/game/TaskBar/anti_exp_02.tga",
							"down_image" : "d:/ymir work/ui/game/TaskBar/anti_exp_03.tga",
						},
						##endif
						{
							"name" : "CostumeButton",
							"type" : "button",

							"x" : 78,
							"y" : 5,

							"tooltip_text" : uiScriptLocale.COSTUME_TITLE,

							"default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
						},						
						{
							"name" : "Equipment_Tab_01",
							"type" : "radio_button",

							"x" : 86,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_01_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "I",
								},
							),
						},
						{
							"name" : "Equipment_Tab_02",
							"type" : "radio_button",

							"x" : 86 + 32,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_02_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "II",
								},
							),
						},

					),
				},

				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",
					"x" : 10,
					"y" : 70 + 191,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,
					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",
					"x" : 10 + 39,
					"y" : 70 + 191,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "II",
						},
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",
					"x" : 10 + 39 + 39,
					"y" : 70 + 191,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,
					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "III",
						},
					),
				},
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",
					"x" : 10 + 39 + 39 + 39,
					"y" : 70 + 191,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,
					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "IV",
						},
					),
				},
## if app.ENABLE_SYSTEM_METINSTONE:
				{
					"name" : "systemss_deutero_button",
					"type" : "button",
					"x" : 92, ## +40 se kathe neo button
					"y" : 225,
					"tooltip_text" : "[ANTI-EXP]",
					"default_image" : "sistimata/button_inventory/anti_exp1.tga",
					"over_image" : "sistimata/button_inventory/anti_exp2.tga",
					"down_image" : "sistimata/button_inventory/anti_exp3.tga",
				},
				{
					"name" : "systemss_tetarto_button",
					"type" : "button",
					"x" : 132, ## +40 se kathe neo button
					"y" : 225,
					"tooltip_text" : "[BONUS-PAGE]",
					"default_image" : "sistimata/button_inventory/bonus_page1.tga",
					"over_image" : "sistimata/button_inventory/bonus_page2.tga",
					"down_image" : "sistimata/button_inventory/bonus_page3.tga",
				},
				{
					"name" : "Button_anthropous",
					"type" : "button",
					"x" : 12,
					"y" : 225,
					"tooltip_text" : uiScriptLocale.ANTHROPOUS_BUTTONS,
					"default_image" : "sistimata/button_inventory/ateleport1.tga",
					"over_image" : "sistimata/button_inventory/ateleport2.tga",
					"down_image" : "sistimata/button_inventory/ateleport3.tga",
				},
##endif
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 8,
					"y" : 285,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				{
					"name" : "Money",
					"type" : "text",
					"x":12,
					"y":28,
					"horizontal_align" : "right",
					"text_horizontal_align" : "right",
					"vertical_align":"bottom",
					"text" : "123456789",
				},
			),
		},
	),
}
