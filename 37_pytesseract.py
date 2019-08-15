import pytesseract
from PIL import Image

im = Image.open('code.png')
print(pytesseract.image_to_string(im))