from PIL import Image
image = Image.open('2.jpg')
cropped = image.crop((0, 100, 30, 860))
cropped.save('2crop.jpg')