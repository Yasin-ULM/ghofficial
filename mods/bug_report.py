# Bug Report Mod v1
# Adds a bunch of buttons to create a bug-report file

# helper functions

def bug_report_write(event=None):
    # add a save file, but without the cfg and rollback
    storage_dict = {'info':'This is a SlutED game bug report file.',
                    'date': Date.new().toLocaleString(),
                    'user_agent': str(data.navigator.userAgent),
                    'game_version': str(data.data_version) +'-'+str(doc['version'].content)}
    storage_dict['inventory'] = inventory.to_string()
    storage_dict['save'] = save.to_string()
    # add the actual bug report
    storage_dict['bug_rep_comment'] = str(doc['bug_rep_comment'].value)
    storage_dict['bug_rep_name'] = str(doc['bug_rep_name'].value)
    storage_dict['bug_rep_next'] = str(doc['bug_rep_next'].value)
    storage_dict['bug_rep_pc'] = str(doc['bug_rep_pc'].value)
    storage_dict['bug_rep_txt'] = str(doc['bug_rep_txt'].value)
    storage_dict['bug_rep_npc'] = str(doc['bug_rep_npc'].value)
    storage_dict['bug_rep_img'] = str(doc['bug_rep_img'].value)
    storage_dict['bug_rep_jump'] = str(doc['bug_rep_jump'].value)
    storage_dict['bug_rep_choice'] = str(doc['bug_rep_choice'].value)
    storage_dict['bug_rep_branch'] = str(doc['bug_rep_branch'].value)
    storage_dict['bug_rep_cmd'] = str(doc['bug_rep_cmd'].value)

    # dict to json
    jdata = JSON.stringify(storage_dict, None, 2)
    # replace newline characters for Firefox
    #jdata = jdata.replace('\n', '%0D%0A')
    # ask user to manually save file, because we have no filesystem access
    doc['bug_rep_save'].href = 'data:text/plain,' + jdata
    #_show('bug_rep_div', False)

def bug_rep_new(event=None):
    doc['bug_rep_comment'].value =''
    for err, node in _error_log:
        doc['bug_rep_comment'].value += str(f'[{node}] : {err}\n')
    if '_current' in data.glob:
        current_bug_node = str(data.glob._current)
        doc['bug_rep_name'].value = current_bug_node
        _show('bug_rep_div')
        if 'next' in data.plot[current_bug_node]:
            doc['bug_rep_next'].value = data.plot[current_bug_node]['next']
        else:
            doc['bug_rep_next'].value = ''

        if 'pc' in data.plot[current_bug_node]:
            doc['bug_rep_pc'].value = data.plot[current_bug_node]['pc']
        else:
            doc['bug_rep_pc'].value = ''

        if 'txt' in data.plot[current_bug_node]:
            doc['bug_rep_txt'].value = data.plot[current_bug_node]['txt']
        else:
            doc['bug_rep_txt'].value = ''

        if 'npc' in data.plot[current_bug_node]:
            doc['bug_rep_npc'].value = data.plot[current_bug_node]['npc']
        else:
            doc['bug_rep_npc'].value = ''

        if 'img' in data.plot[current_bug_node]:
            doc['bug_rep_img'].value = data.plot[current_bug_node]['img']
        else:
            doc['bug_rep_img'].value = ''

        if 'eval_jump_to' in data.plot[current_bug_node]:
            doc['bug_rep_jump'].value = data.plot[current_bug_node]['eval_jump_to']
        else:
            doc['bug_rep_jump'].value = ''

        if 'choice' in data.plot[current_bug_node]:
            choice_dump = ''
            for choice_condition, choice_label, choice_target in data.plot[current_bug_node]['choice']:
                choice_dump+= str(f'["{choice_condition}", "{choice_label}", "{choice_target}"]\n')

            doc['bug_rep_choice'].value = choice_dump
        else:
            doc['bug_rep_choice'].value = ''

        if 'branch' in data.plot[current_bug_node]:
            branch_dump = ''
            for branch_condition, branch_target in data.plot[current_bug_node]['branch']:
                branch_dump+= str(f'["{branch_condition}", "{branch_target}"]\n')

            doc['bug_rep_branch'].value = branch_dump
        else:
            doc['bug_rep_branch'].value = ''

        if 'cmd' in data.plot[current_bug_node]:
            cmd_dump = ''
            for cmd in data.plot[current_bug_node]['cmd']:
                cmd_dump+= str(cmd)+'\n'

            doc['bug_rep_cmd'].value = cmd_dump
        else:
            doc['bug_rep_cmd'].value = ''
    else:
        doc['bug_rep_comment'].value += 'Error making error report! Unknown node '
        print (data.glob)

# make the panel for the mod with a button, rest added later...

mod_panel = add_mod_cfg('Bug Report v1', { 'Generate Bug Report': bug_rep_new})

# add instructions
mod_panel.appendChild(html.BR())
mod_panel.appendChild(html.DIV("Click on the 'Generate Bug Report' to start."))

bug_rep_div = html.DIV(id="bug_rep_div", style={'display': 'none'})
# add all the things...

# user comment
bug_rep_div.appendChild(html.DIV("DESCRIBE THE ERROR:"))
bug_rep_div.appendChild(html.DIV("(if it's a typo or spelling mistake - just edit the text field below)"))
bug_rep_div.appendChild(html.TEXTAREA(id="bug_rep_comment", rows="6", cols="60"))
bug_rep_div.appendChild(html.BR())
bug_rep_div.appendChild(html.BR())

# suggest a fix
bug_rep_div.appendChild(html.DIV("SUGGEST A FIX:"))
bug_rep_div.appendChild(html.DIV("You can edit the fields below if you know how to fix the error you have encountered."))
# text (textarea)
bug_rep_div.appendChild(html.DIV("Text:"))
bug_rep_div.appendChild(html.TEXTAREA(id="bug_rep_txt", rows="6", cols="60"))
bug_rep_div.appendChild(html.BR())
# node name (id)
bug_rep_div.appendChild(html.SPAN("Node Name:"))
bug_rep_div.appendChild(html.INPUT(type="text", id="bug_rep_name", size="30"))
bug_rep_div.appendChild(html.BR())
# next
bug_rep_div.appendChild(html.SPAN("Next Node ID:"))
bug_rep_div.appendChild(html.INPUT(type="text", id="bug_rep_next", size="30"))
bug_rep_div.appendChild(html.BR())

# PC
bug_rep_div.appendChild(html.SPAN("PC:"))
bug_rep_div.appendChild(html.INPUT(type="text", id="bug_rep_pc", size="30"))
bug_rep_div.appendChild(html.BR())
# npc
bug_rep_div.appendChild(html.SPAN("NPC:"))
bug_rep_div.appendChild(html.INPUT(type="text", id="bug_rep_npc", size="30"))
bug_rep_div.appendChild(html.BR())

# img
bug_rep_div.appendChild(html.SPAN("Image:"))
bug_rep_div.appendChild(html.INPUT(type="text", id="bug_rep_img", size="30"))
bug_rep_div.appendChild(html.BR())
# eval_jump_to
bug_rep_div.appendChild(html.SPAN("Jump:"))
bug_rep_div.appendChild(html.INPUT(type="text", id="bug_rep_jump", size="30"))
bug_rep_div.appendChild(html.BR())


# choices (textarea dump)
bug_rep_div.appendChild(html.DIV("Choices:"))
bug_rep_div.appendChild(html.TEXTAREA(id="bug_rep_choice", rows="6", cols="60", wrap="off"))
bug_rep_div.appendChild(html.BR())
# branches (textarea dump)
bug_rep_div.appendChild(html.DIV("Branches:"))
bug_rep_div.appendChild(html.TEXTAREA(id="bug_rep_branch", rows="6", cols="60", wrap="off"))
bug_rep_div.appendChild(html.BR())

# cmds (textarea dump)
bug_rep_div.appendChild(html.DIV("Commands:"))
bug_rep_div.appendChild(html.TEXTAREA(id="bug_rep_cmd", rows="6", cols="60", wrap="off"))
bug_rep_div.appendChild(html.BR())
# save/download button
bug_rep_div.appendChild(html.DIV("Click the button below to save a bug report file:"))
bug_rep_div.appendChild(html.A('WRITE FILE', Class="cfg_button", id="bug_rep_save", href="", download="bug_report.txt"))
#add the div
mod_panel.appendChild(bug_rep_div)

#bind the  button
doc['bug_rep_save'].bind('mousedown', bug_report_write)

# announce we're done
print('Bug Report Mod v1 installed!')
