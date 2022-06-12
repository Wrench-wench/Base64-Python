import base64Convert
import base64

with open("preferences-color.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    print(my_string)

base64Convert.saveimage(my_string)
