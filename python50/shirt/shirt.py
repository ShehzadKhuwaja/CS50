import sys
import os
from PIL import Image 
from PIL import ImageOps

    
def get_extn(file_name):
    _, ext = os.path.splitext(file_name)
    return ext.lower() 

valid_extensions = [".jpg", ".jpeg", ".png"]
if len(sys.argv[1:]) != 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv[1:]) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif get_extn(sys.argv[2]) not in valid_extensions:
    print("Invalid output")
    sys.exit(1)
elif get_extn(sys.argv[1]) != get_extn(sys.argv[2]):
    print("Input and output have different extensions")
    sys.exit(1)


try:
    person = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    print("Input does not exist")
    sys.exit(1)

person = ImageOps.fit(person, size=shirt.size)
person.paste(shirt, mask=shirt)
person.save(sys.argv[2])
