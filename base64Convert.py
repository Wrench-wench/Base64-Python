import base64
from PIL import Image
from io import BytesIO

def saveimage(base64str):
    # TODO add in an optional name for the saved file.

    im = Image.open(BytesIO(base64.b64decode(base64str)))
    im.save('image.png', 'PNG')

f = open('base64.txt', 'r')
data = f.read()
f.closed

saveimage(data)