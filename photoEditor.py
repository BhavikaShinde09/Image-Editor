from PIL import Image, ImageEnhance, ImageFilter
import os

path = "IMG_3583.JPG"
pathOut = '\editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).rotate(-90).convert('L')

    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
