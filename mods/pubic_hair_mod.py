# Pubic Hair Mod v2 for SlutED
# Adds pubic hair to the avatar/paperdoll
# and a set of buttons to the mod menu to customize the look
# some assets made by: mrnow19
# This is a sample mod, made to demonstrate how mods work.
# Note: The current Mod Manager gets confused by some comments
#       Do not use multiline comments with triple quotes.
#       Do not use inline comments on end of the lines

# Add an extra <img> tag to the existing avatar image stack
bush_img = html.IMG(id='pc_img_pubic_hair', alt='bush', Class="pc_img", srcset="mods/sample_mods_data/bush.png", style={'display': 'none'})
# the bush image must go after the nude img, but before the clothing (stockings)
doc['pc_imgs'].insertBefore(bush_img, doc['pc_img_underwear_bottom'])
# we need to wrap the show_pc() function
# in a new function that runs the original show_pc() code and also shows our newly added hair
def monkey_patch_function(func):
    def wrapped(*args, **kwargs):
        # run the original function,
        # in this case it returns nothing
        func(*args, **kwargs)
        # run our little extra code
        # check if we need to show or hide
        visible = True
        if 'visible' in kwargs:
            visible =  kwargs['visible']
        elif args:
            visible = args[0]
        # we'll use the _show() function to reduce boilerplate code
        _show('pc_img_pubic_hair', visible)
        # we'll also set a flag in the save
        # this way npc can react, or images can be replaced later on
        save.mod_pubic_hair = 1
    return wrapped

# now we replace the original show_pc() with our patched version
show_pc = monkey_patch_function(show_pc)
# new version - we add buttons to the mod menu

# helper function to change the image and save it for later
def set_pub_hair(img):
    doc['pc_img_pubic_hair'].srcset = img
    save.mod_pubic_hair_img = img

# add_mod_cfg is a helper function that will set up the right section in the mod menu
# it needs a display name and a dictionary of buttons
# the dictionary of buttons should have the text as a key and a function as a value
# we use a lambda here to pass in a function with arguments
buttons = { 'Shaved': lambda x: set_pub_hair('mods/sample_mods_data/shaved.png'),
            'Bush': lambda x: set_pub_hair('mods/sample_mods_data/bush.png'),
            'Heart': lambda x: set_pub_hair('mods/sample_mods_data/heart.png'),
            'Strip': lambda x: set_pub_hair('mods/sample_mods_data/landing_strip.png'),
            'Small Strip': lambda x: set_pub_hair('mods/sample_mods_data/landing_strip_small.png'),
            'Stubble': lambda x: set_pub_hair('mods/sample_mods_data/stubble.png'),
            'Triangle': lambda x: set_pub_hair('mods/sample_mods_data/triangle.png'),
          }
add_mod_cfg('Pubic Hair Mod v2', buttons)

#we should check if there is a previous saved image
if save.mod_pubic_hair_img:
    doc['pc_img_pubic_hair'].srcset = save.mod_pubic_hair_img

# announce we're done
print('Pubic Hair Mod v2 installed!')
