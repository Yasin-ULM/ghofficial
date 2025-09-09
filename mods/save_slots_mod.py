# Save Slots v3 Mod for SlutED
# This mod adds save and load slots
# NOTE: This mod may break the game if the browsers localStorage quota is exceeded!

save_mod_num_slots = 8

def save_mod_guess_storage_size():
    total_data=''
    for key in data.localStorage:    
        if data.localStorage.hasOwnProperty(key):
            total_data += data.localStorage.getItem(key)
            total_data += key    
    #return round((len(total_data) * 16)//(8 * 1024), 2)
    return round(len(total_data) * 0.001953125, 2)

def save_mod_save(event):
    slot = int(event.target.id[14:])
    print('saving to slot '+str(slot))
    smod_save[slot] = DataStore('save_'+str(slot))
    smod_inventory[slot] = DataStore('inventory_'+str(slot))
    smod_quests[slot] = DataStore('quests_'+str(slot))

    smod_save[slot].from_string(save.to_string())
    smod_inventory[slot].from_string(inventory.to_string())
    smod_quests[slot].from_string(quests.to_string())
    _show('modal_box', False)

def save_mod_load(event):
    # id='save_mod_slot_'+str(i))
    slot = int(event.target.id[14:])
    print('loading from slot '+str(slot))
    save.from_string(smod_save[slot].to_string())
    inventory.from_string(smod_inventory[slot].to_string())
    quests.from_string(smod_quests[slot].to_string())
    # rollback
    rollback_save.clear()
    rollback_inventory.clear()
    rollback_quests.clear()
    _show('modal_box', False)
    move_to('load_last')

def save_mod_show_saves(event=None):
    elements=[]
    for i in range(1,save_mod_num_slots+1):
        b1 = html.BUTTON('LOAD', type='button', Class='mod_button', id='save_mod_slot_'+str(i))
        text=f'{i}: [EMPTY]'
        if DataStore.exists('inventory_'+str(i)):
            smod_inventory[i] = DataStore('inventory_'+str(i))
            smod_save[i] = DataStore('save_'+str(i))
            smod_quests[i]= DataStore('quests_'+str(i))
            time = smod_save[i]['time']
            day, hour = divmod(time, 24)
            time_name = TIME.TIME_NAMES[hour//4]
            day_name = TIME.DAY_NAMES[int(day%7)]
            text = f'{i}: Day {day}, {day_name} {time_name}'            
            b1.bind('click', save_mod_load)

        d=html.DIV(text)        
        b2 = html.BUTTON('SAVE', type='button', Class='mod_button', id='save_mod_slot_'+str(i))
        b2.bind('click', save_mod_save)        
        d.appendChild(b1)
        d.appendChild(b2)
        elements.append(d)

    mem_left = int(100 - round((save_mod_guess_storage_size()/2000.0) +0.5))
    elements.append(html.DIV('Storaged left: ~'+str(mem_left)+'%'))        
    _show_modal('Save/Load:', elements, None)

if 'in_memory_storage' in data.glob:    
    show_error("Warning: Game uses in-memory-storage, Save Slots Mod DISABLED.")               
else:    
    smod_save = {}
    smod_inventory = {}
    smod_quests = {}

    # add a save icon/button to the left corner div
    doc['left_corner'].appendChild(html.DIV(chr(int('f0c7', 16)),id='save_mod_button', Class='icon_button_aws'))

    doc['save_mod_button'].bind('click', save_mod_show_saves)

    #print('Storage used: ~'+str(save_mod_guess_storage_size())+'KB out of 2000KB')
    print('Save Slots v3 Mod installed!')
