# BINARY FILE HANDELING

with open('cat.jpeg','rb') as file:
    # print(file.read())
    data = file.read()
    print(type(data)) # <class 'bytes'>
    print(len(data))

from PIL import Image

img = Image.open('cat.jpeg')
img.show()