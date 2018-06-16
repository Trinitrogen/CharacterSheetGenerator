from PIL import Image, ImageDraw, ImageFont
import os


coords =  (105,396)
im = Image.open('CharacterSheet.png')
draw = ImageDraw.Draw(im)
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 25)
draw.text(coords, '17', font=fnt, fill='black')
im.save('Output.png')