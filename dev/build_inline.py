import os
import base64

pack_mp3 = True
pack_img = True

img_source = '../img'
audio_source = '../audio'

def get_file_content(file_path):
    data=''
    with open(file_path, 'r') as f:
        data= f.read()
    return data    

def pack_file(file_name, target):
    print('Encoding: '+file_name, end=' ')  
    with open(file_name, 'rb') as in_file:
        if file_name.endswith('webm') or file_name.endswith('xxx'):
            mime = 'data:video/webm; base64, '
        elif file_name.endswith('png'):
            mime = 'data:image/png; base64, '
        elif file_name.endswith('webp'):
            mime = 'data:image/webp; base64, '
        elif file_name.endswith('jpeg'):
            mime = 'data:image/jpeg; base64, '  
        elif file_name.endswith('jpg'):
            mime = 'data:image/jpeg; base64, '  
        elif file_name.endswith('mp3'):
            mime = 'data:audio/mpeg; base64, '    
        else:
            mime= 'data: application/octet-streaml base64'  
        target[file_name[3:]] = mime+base64.b64encode(in_file.read()).decode('ascii')
    print('done.')


encoded_img = {}
if pack_img:
    for file_name in os.listdir(img_source):
        if os.path.isdir(img_source+'/'+file_name):
            print(file_name, 'is dir')
            for sub_file_name in os.listdir(img_source+'/'+file_name):
                pack_file(img_source+'/'+file_name+'/'+sub_file_name, encoded_img)
        else:   
            pack_file(img_source+'/'+file_name, encoded_img)

encoded_mp3 = {}
if pack_mp3:
    for file_name in os.listdir(audio_source):       
        pack_file(audio_source+'/'+file_name, encoded_mp3)

combined_style =''
with open('../index_inline.html', 'w+') as out_file:
    with open('../index.html', 'r') as in_file:
        for line in in_file:
            if line.strip().startswith('<meta name="version"'):
                v = line.strip().split('=')[2].split()[0].strip('"')
                out_file.write(f'        <meta name="version" content="{v}.i" id="version">')
            elif line.strip().startswith('<link rel="stylesheet" href='):                
                style_sheet_path = line.strip().strip('>').removeprefix('<link rel="stylesheet" href=').strip('"')
                print('Packing stylesheet: '+style_sheet_path, end=' ')
                combined_style += get_file_content('../'+style_sheet_path)
                print('done')
            elif line.strip().startswith('<script type="text/javascript" src='):
                script_path = line.strip().split('=')[2].removesuffix('></script>').strip('"')
                print('Packing script: '+script_path, end=' ')
                out_line = '<script type="text/javascript">\n'
                out_line +=get_file_content('../'+script_path)
                out_line += '\n</script>\n'
                out_file.write(out_line)
                print('done')
            elif line.strip().startswith('</head>'):
                print('Writing images...')
                out_file.write( '<script type="text/javascript">\n var images = {\n')                
                for k,v in encoded_img.items():
                    print(f'Writing: {k}', end=' ')
                    out_file.write(f'"{k}" : "{v}",\n') 
                    print('done')     
                out_file.write("};\n")
                print('Writing audio...')
                out_file.write( 'var sounds = {\n')
                for k,v in encoded_mp3.items():
                    print(f'Writing: {k}', end=' ')
                    out_file.write(f'"{k}" : "{v}",\n') 
                    print('done')     
                out_file.write("};\n</script>\n")

                print('Writing combined style...', end=' ')
                combined_style = combined_style.replace('../', '')
                out_line = '<style>\n'+combined_style+'\n</style>\n</head>\n'
                out_file.write(out_line)
                print('done')
            else:
                out_file.write(line)

print('All done.')