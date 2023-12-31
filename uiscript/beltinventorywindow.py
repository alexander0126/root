import uiScriptLocale
import item

EQUIPMENT_START_INDEX = 180

window = {
	"name" : "BeltInventoryWindow",

	"x" : SCREEN_WIDTH - 176 - 148,
	"y" : SCREEN_HEIGHT - 37 - 565 + 209 + 32,

	"width" : 148,
	"height" : 139,

	"type" : "image",
	"image" : "d:/ymir work/ui/game/belt_inventory/bg.tga",
	

	"children" :
	(
		{
			"name" : "ExpandBtn",
			"type" : "button",

			"x" : 2,
			"y" : 15,

			"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga",
			"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga",
			"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga",
			"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_disabled.tga",
		},

		
		{
			"name" : "BeltInventoryLayer",

			"x" : 5,
			"y" : 0,

			"width" : 148,
			"height" : 139,

			"children" :
			(
				{
					"name" : "MinimizeBtn",
					"type" : "button",

					"x" : 2,
					"y" : 15,

					"width" : 10,

					"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga",
					"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga",
					"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga",
					"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_disabled.tga",
				},

				{
					"name" : "BeltInventoryBoard",
					"type" : "board",
					"style" : ("attach", "float"),

					"x" : 10,
					"y" : 0,

					"width" : 138,
					"height" : 139,

					"children" :
					(
						{
							"name" : "BeltInventorySlot",
							"type" : "grid_table",

							"x" : 5,
							"y" : 5,

							"start_index" : item.BELT_INVENTORY_SLOT_START,
							"x_count" : 4,
							"y_count" : 4,
							"x_step" : 32,
							"y_step" : 32,

							"image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
					),
				},
			)
		},

	),
}
