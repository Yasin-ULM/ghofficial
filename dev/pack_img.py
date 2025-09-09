import sys
import os
import base64

#source = sys.argv[1]
source = '../img'

def pack_img(file_name, target):
	print('Encoding: ', file_name)	
	with open(file_name, 'rb') as in_file:
		if file_name.endswith('webm'):
			mime = 'data:video/webm; base64, '
		elif file_name.endswith('png'):
			mime = 'data:image/png; base64, '
		elif file_name.endswith('webp'):
			mime = 'data:image/webp; base64, '
		elif file_name.endswith('jpeg'):
			mime = 'data:image/jpeg; base64, '	
		elif file_name.endswith('jpg'):
			mime = 'data:image/jpeg; base64, '	
		else:
			mime= 'data: application/octet-streaml base64'	
		target[file_name[3:]] = mime+base64.b64encode(in_file.read()).decode('ascii')
	print('Encoding done.')


encoded = {}
for file_name in os.listdir(source):
	if os.path.isdir(source+'/'+file_name):
		print(file_name, 'is dir')
		for sub_file_name in os.listdir(source+'/'+file_name):
			pack_img(source+'/'+file_name+'/'+sub_file_name, encoded)
	else:	
		pack_img(source+'/'+file_name, encoded)

i=0
with open('../data/imgdata.txt', 'w') as out_file:
	out_file.write("var images = {\n")
	for k,v in encoded.items():
		out_file.write(f'"{k}" : "{v}",\n')	
		print(f'writing: {k}')	
		i+=1	
	out_file.write("};")
	
	

print(f'TOTAL FILES PACKED: {i}/{len(encoded)}')	

os.system('pause')	