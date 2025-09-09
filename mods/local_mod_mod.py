# Local Mod Mod v1 for SlutED
# allows loading mods from local files (even if the game is run online)
# This is a sample mod, made to demonstrate how mods work.


# helper functions

def load_mod(event=None):
    def _on_load(event):
        raw_mod_source = event.target.result
        try:
            exec(raw_mod_source)
        except Exception as e:
            print(str(e))
    mod_file = doc['import_mod'].files[0]
    # window is data
    reader = data.FileReader.new()
    reader.readAsText(mod_file)
    reader.bind('load', _on_load)


# add_mod_cfg is a helper function that will set up the right section in the mod menu
mod_panel = add_mod_cfg('Load Local Mod Mod v1', {})
mod_panel.appendChild(html.BR())
# add a file input widget
# we wrap it in a label because else you can't style it
label = html.LABEL('Select mod file...', Class="mod_button")
mod_file_input = html.INPUT(type="file", id="import_mod", name="import_mod")
mod_file_input.bind('input', load_mod)
label.appendChild(mod_file_input)
mod_panel.appendChild(label)
mod_panel.appendChild(html.BR())
# announce we're done
print('Local Mod Mod v1 installed!')
