from email import message
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

from images import get_image
from quotes import get_quote
from constants import IMAGE_PATH, POSTER_PATH


get_image()
quote = get_quote()

def get_poster():
    img = Image.open(IMAGE_PATH)
    img_w, img_h = img.size

    draw = ImageDraw.Draw(img)

    # font = ImageFont.truetype(<font-file>, <font-size>)
    font_size = 50

    font = ImageFont.truetype("arial.ttf", font_size)

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((int(img_w / 2) - (int(len(quote.message) / 2) * int(font_size / 2)), int(img_h / 2) - font_size),quote.message,(0, 0, 0),font=font)
    img.save(POSTER_PATH)
