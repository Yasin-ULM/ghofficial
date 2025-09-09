'''
Script to convert a dir of images(png/jpg) to .webp
libwebp needs to be installed and present (on path)
get it here:
https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html
'''
import os
import sys

options = ['-alpha_q 100',
            '-q 95',
            '-m 5']

args_dict = {}
if len(sys.argv) == 3:
    args_dict['source_dir'] = sys.argv[1]
    args_dict['target_dir'] = sys.argv[2]
elif len(sys.argv) == 2:
    args_dict['source_dir'] = sys.argv[1]
    args_dict['target_dir'] = sys.argv[1]
elif len(sys.argv) > 3:
    args_dict['source_dir'] = sys.argv[1]
    args_dict['target_dir'] = sys.argv[2]
    options =  sys.argv[3:]
else:
    print('Usage:')
    print('python webpy.py source_dir [target_dir] [cwebp_args]')



cmd = 'cwebp {source_dir}/{filename}'

for opt in options:
    cmd+= ' '+opt+' '
cmd += '-o {target_dir}/{basename}.webp'

img_types = ['.png', '.jpg']
if  os.path.exists(args_dict['source_dir']):
    if not os.path.exists(args_dict['target_dir']):
        os.mkdir(args_dict['target_dir'])

    for filename in os.listdir(args_dict['source_dir']):
        basename, ext = os.path.splitext(filename)
        if ext in img_types:
            args_dict['basename'] = basename
            args_dict['filename'] = filename
            os.system(cmd.format(**args_dict) )
else:
    print('No such directory: '+args_dict['source_dir'])
