
def mod_ww_close_shop(event=None):
    if int(save.money) < 0:
        _restart_anim('wear_money', 'blink_red')
        return
    #else:
    save.remove('last_shopping_cart')
    _show(['buy_grid', 'sell_grid', 'cloths','outfit_grid'], False)
    show_pc(False)
    current_clothes = []
    for item_id, item_slot in inventory.items():
        if item_slot:
            current_clothes.append(item_id)
    if not save.last_shop_limited:
        save.set_list('_current_clothes', current_clothes)
    # show rollback
    if not rollback_save.is_empty():
        _show('rollback')
    # show questlog
    if not quests.is_empty():
        _show('questlog')
    history_log_txt = '[ Changed clothes to: '
    for item_id, slot in inventory.items():
        if slot:
            name = data.items[item_id]['name']
            if name != '- Nothing -':
                history_log_txt+= name+', '
    history_log_txt += str(save.current_slut)+' ]'
    doc['history_txt'].textContent += history_log_txt

    # loopback shop - do not use in plot nodes!
    if save.last_shop_loopback:
        save.remove('last_shop_loopback')
        move_to(save.current_plot_node)
        return
    save.remove('last_shop_loopback')

    # progress to next node
    _move_to_next()

doc['shop_close'].unbind('click')
doc['shop_close'].bind('click', mod_ww_close_shop)

print('Wear Whatever Mod installed!')
