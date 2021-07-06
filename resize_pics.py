import os
from PIL import Image

for file in os.listdir('.'):
    if os.path.isdir(file):
        for img_file in os.listdir(file):
            try:
                im = Image.open(file+'/'+img_file).convert('RGB')
                im = im.resize((200, 200))
                im.save(file+'/'+img_file)
                print('Resized {}'.format(file+'/'+img_file))
            except Exception:
                print('Error involving {}'.format(file+'/'+img_file))