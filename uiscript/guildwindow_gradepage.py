import uiScriptLocale

window = {
	"name" : "GuildWindow_BoardPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		## GradeNumber
		{
			"name" : "GradeNumber", "type" : "image", "x" : 17, "y" : 0, "image" : "sistimata/suntexnia/1.tga",
		},
		## GradeName
		{
			"name" : "GradeName", "type" : "image", "x" : 48, "y" : 0, "image" : "sistimata/suntexnia/2.tga",
		},
		## InviteAuthority
		{
			"name" : "InviteAuthority", "type" : "image", "x" : 104, "y" : 0, "image" : "sistimata/suntexnia/3.tga",
		},
		## DriveOutAuthority
		{
			"name" : "DriveOutAuthority", "type" : "image", "x" : 157, "y" : 0, "image" : "sistimata/suntexnia/4.tga",
		},
		## NoticeAuthority
		{
			"name" : "NoticeAuthority", "type" : "image", "x" : 209, "y" : 0, "image" : "sistimata/suntexnia/5.tga",
		},
		## GeneralAuthority
		{
			"name" : "GeneralAuthority", "type" : "image", "x" : 254, "y" : 0, "image" : "sistimata/suntexnia/6.tga",
		},
		#if app.ENABLE_WAR_PERMISSION:
		{
			"name" : "WarAuthority", "type" : "image", "x" : 305, "y" : 0, "image" : "sistimata/suntexnia/7.tga",
		},

	),
}
