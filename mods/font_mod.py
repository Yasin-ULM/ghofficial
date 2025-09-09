# Font mod
# replaces the default Monofonto font used for text with Atkinson Hyperlegible 

def set_font(font_name):
	doc['txt'].style['font-family'] = font_name

buttons = { 'Atkinson Hyperlegible': lambda x: set_font('atkinson'),
            'Monofonto': lambda x: set_font('monofonto'),            
          }
add_mod_cfg('Font Mod v1', buttons)

# announce we're done
print('Font Mod v1 installed!')
