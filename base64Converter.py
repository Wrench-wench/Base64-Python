from PIL import Image
from io import BytesIO
import base64
import string
import json

def convert_to_image(base64str: str, filename: str, file_extension: str):

    try:
        filename = filename.split(".")
        filename = filename[0]
        filename = filename.translate(str.maketrans('', '', string.punctuation))
        file_extension = file_extension.translate(str.maketrans('', '', string.punctuation))
        base64str = str(base64str)
    except Exception as err:
        print(err)
        exit()

    name = f"{filename}.{file_extension}"

    im = Image.open(BytesIO(base64.b64decode(base64str)))
    im.save(name, file_extension)
    im.close
    print(f'{name} saved.')
    return


def convert_to_base64(filename: str):
    # Get file name and extension
    name = filename.split(".")
    file_extension = name[-1]
    name = name[1]

    # Open the file and convert to base64 string
    with open(filename, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read())

    # Put everything in to JSON
    base64_object = json.dumps({
        "Filename": filename,
        "File Extension": file_extension,
        "base64_string" : str(base64_string), # A bytes object is not JSON serialable, so convert to string
        }, indent=4)

    return base64_object

if __name__ == "__main__":
    print('Hello!')

    # Test using a base64 string
    with open('base64.txt', 'r') as file:
        base64str = file.readline()
        convert_to_image(base64str=base64str, filename='base64', file_extension='png')

    # Test using an image
    base64JSON = convert_to_base64(filename='preferences-color.png')
    print(base64JSON)
    exit()
