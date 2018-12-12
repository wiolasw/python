import PIL
from PIL import Image
from os import listdir
from os.path import splitext

sciezka = 'C:/Users/wiola/PycharmProjects/ZALICZENIE_PYTHON/Pythone_1'
format = '.png'

for file in listdir(sciezka):
    filename, extension = splitext(file)
try:
    if extension not in ['.py', format]:
        im = Image.open(filename + extension)
        im.save(filename + format)


except OSError:
    print('Cannot convert %s' % file)