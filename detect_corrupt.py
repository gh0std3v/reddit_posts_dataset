import os
from PIL import Image

for dirfile in os.listdir('.'):
    if os.path.isdir(dirfile) and '.git' not in dirfile:
        for file in os.listdir(dirfile):
            try:
                name = dirfile+'/'+file
                im = Image.open(name)
                im.verify()
            except (IOError, SyntaxError) as e:
                print('Found corrupt image file {}'.format(name))