# Hide Mod v1 for SlutED
# Removes the icon and changes the title page to 'Untitled 1'
# This is a sample mod, made to demonstrate how mods work.
# Note: The current Mod Manager gets confused by some comments
#       Do not use multiline comments with triple quotes.
#       Do not use inline comments on end of the lines

doc['favico1'].href = 'img/potato.ico'
doc['favico2'].href = 'img/potato.ico'
doc['title'].textContent = 'Untitled 1'

# announce we're done
print('Hide Mod v1 installed!')
