from PIL import Image
from PIL import Image , ImageDraw, ImageFont
#  Исходное изображение
picture = Image.open('Grand_can.jpg')
picture.show()
#  Обрезка изображения
cord = (100, 100, 1200, 800) # лево, верх, право, низ
new_picture = picture.crop(cord)
new_picture.show()
#  Изменение  размера изображения
resized_image = picture.resize((1280, 620))
resized_image.show()
#  Надпись  на изображении
font = ImageFont.truetype("arial.ttf", 96, encoding="unic")
pencil = ImageDraw.Draw(resized_image)
pencil.text((200,200),'GRAND  CANYON',  font=font, size = 256)
resized_image.show()