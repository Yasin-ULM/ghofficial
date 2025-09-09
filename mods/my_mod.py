#This is a sample mod, whatever....

my_new_items = {
	"xmas_socks":{
	    "name":"Xmas Socks",
	    "img":"mods/my_mod/xmas_socks.png",
	    "slot":"stockings",
	    "tags":['stockings'],
	    "slutty":0,
	    "value":20
	    },
	"xmas_dress":{
	    "name":"Xmas Dress",
	    "img":"mods/my_mod/xmas_dress.png",
	    "slot":"top",
	    "tags":['clothes_top', 'clothes_bottom', 'cover_boobs', 'partial_cover_boobs'],
	    "slutty":0,
	    "value":30
	    },
}

#add the items to the global items 
for itm_id, itm_data in my_new_items.items():
	data.items[itm_id] = itm_data

#add the items to a shop
data.shops['dress_shop'].append('xmas_dress')
data.shops['dress_shop'].append('xmas_socks')

#print that we installed the mod
print('Bla, bla, bla.. installed mod or something....')