'''
Python script to make datalists (hints) for the editor,
copy/paste the output
'''
import os

img_datalists = {
            'imgs':['../img'],
            'npcs':['../img/npc']
            }

exclude_subdirs ={
            'imgs':['pc', 'npc', 'cocos', 'portrait', 'big', 'panorama', 'parallax', 'svg'],
            'npcs':[]
            }

def print_img_datalist(id_name, paths, exclude):
    print(' '*8+f'<datalist id="{id_name}">')
    for img_path in paths:
        for path, subdirs, files in os.walk(img_path):
            if os.path.split(path)[-1] not in exclude:
                for name in files:
                    filename, extension = os.path.splitext(name)
                    if extension in ('.png', '.jpg', '.jpeg', '.webp', '.gif', '.xxx'):
                        if path.startswith('../'):
                            url_path = path[3:].replace('\\', '/')
                        else:
                            url_path = path.replace('\\', '/')
                        print(' '*12+f'<option value="{url_path}/{name}">')
    print(' '*8+'</datalist>')


for id_name, paths in img_datalists.items():
    print_img_datalist(id_name, paths, exclude_subdirs[id_name])


# look for public API
print(' '*8+'<datalist id="cmds">')
#add big images
for path, subdirs, files in os.walk('../img/big'):
    for img_name in files:
        print(' '*12+f'''<option value="parallax_imgs('img/big/{img_name}')">''')

with open('../index.html') as sourcecode:
    for line in sourcecode.readlines():
        if line.startswith('        def'):
            f = line.strip().strip('def').strip(':').strip()
            if not f.startswith('_'):
                print(' '*12+f'<option value="{f}">')
print(' '*8+'</datalist>')
