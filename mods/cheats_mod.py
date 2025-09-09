# Cheat Mod v1.1 for SlutED
# adds buttons that give money, change slut values, show map,
# give clothes and allow changing clothes at any moment
# This is a sample mod, made to demonstrate how mods work.
# Note: The current Mod Manager gets confused by some comments
#       Do not use multiline comments with triple quotes.
#       Do not use inline comments on end of the lines


# helper functions
def cheat_give_100(event=None):
    save.money += 100

def cheat_slut(event=None):
    save.max_slut += 1

def cheat_exec(event=None):
    ''' Execute the command typed into the console
    '''
    cmd = doc['cheat_console'].value
    if cmd:
        try:
            exec(cmd)
        except Exception as e:
            print(str(e))

def cheat_teleport_home(event=None):
    # set default filter
    svg_filter('default')
    # remove overlays
    overlay_img(None)
    # remove body overlays
    set_body_overlay(None)
    # put on clothes if we don't have any on:
    if not get_equipped():
        needed_slots = ['top', 'bottom', 'underwear_top', 'underwear_bottom']
        items_to_equip = []
        for itm_id, slot in inventory.items():
            if needed_slots and itm_id in data.items:
                target_slot = data.items[item_id]['slot']
                if target_slot in needed_slots:
                    items_to_equip.append(itm_id)
                    del needed_slots[needed_slots.index(target_slot)]
        if items_to_equip:
            set_clothes(items_to_equip)
    # end time critical events
    remove_tce()
    # set current_location to map_home
    save.current_location = 'map_home'
    # jump to map_home - this might still trigger events
    move_to('map_home')

# add_mod_cfg is a helper function that will set up the right section in the mod menu
# it needs a display name and a dictionary of buttons
# the dictionary of buttons should have the text as a key and a function as a value
# we use a lambda here to pass in a function with arguments
buttons = { '+ $100': cheat_give_100,
            '+1 Max Slut': cheat_slut,
            'Change Clothes': lambda x: change_clothes(enforce_stats=0, loopback=True),
            'All School Clothes': lambda x: give_clothes_by_tag('school'),
            'All Sport Clothes': lambda x: give_clothes_by_tag('sport'),
            'All Maid Clothes': lambda x: give_clothes_by_tag('maid'),
            'Teleport Home': cheat_teleport_home,
          }
mod_panel = add_mod_cfg('Cheat Mod v1', buttons)
# we add a input box for a console into the mod panel
# ...after a newline...
mod_panel.appendChild(html.BR())
# ...and some text
mod_panel.appendChild(html.SPAN('Python Console:'))
# the input box
mod_panel.appendChild(html.INPUT(type='text', size='50', id='cheat_console'))
# extra button
exec_button = html.BUTTON(' exec ', type='button')
exec_button.bind('click', cheat_exec)
mod_panel.appendChild(exec_button)

# announce we're done
print('Cheat Mod v1 installed!')
