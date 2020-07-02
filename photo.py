from PIL import Image
from PIL import ImageOps
import requests
import os


def photokek(url):
    p = requests.get(url)
    out = open("img.jpg", "wb")
    out.write(p.content)
    out.close()

    im = Image.open("img.jpg")
    half_left = im.copy()
    photo2 = im.copy()
    x, y = im.size
    half_x = int(x / 2)
    half_left = half_left.crop((0, 0, half_x, y))
    half_left = half_left.transpose(Image.FLIP_LEFT_RIGHT)
    photo2.paste(half_left, (half_x, 0))
    half_right = im.copy()
    half_right = half_right.crop((half_x, 0, x, y))
    half_right = half_right.transpose(Image.FLIP_LEFT_RIGHT)
    photo1 = im.copy()
    photo1.paste(half_right, (0, 0))
    photo1.save('photo1.jpg')
    photo2.save('photo2.jpg')
    os.remove("img.jpg")


def invert(url):
    p = requests.get(url)
    out = open("imginvert.jpg", "wb")
    out.write(p.content)
    out.close()

    im = Image.open("imginvert.jpg")
    inverted_image = ImageOps.invert(im)

    inverted_image.save('imginverted.jpg')
    os.remove("imginvert.jpg")


def make_3d(url, delta=10):
    p = requests.get(url)
    out = open("img3d.jpg", "wb")
    out.write(p.content)
    out.close()

    im1 = Image.open("img3d.jpg")
    im2 = im1.copy()
    pixels2 = im2.load()
    pixels1 = im1.load()
    x, y = im1.size
    for i in range(x):
        for j in range(y):
            if i - delta >= 0:
                r = pixels2[i - delta, j][0]
                g = pixels1[i, j][1]
                b = pixels1[i, j][2]
                pixels1[i, j] = r, g, b
            else:
                g = pixels1[i, j][1]
                b = pixels1[i, j][2]
                pixels1[i, j] = 0, g, b
    im1.save('imgres3d.jpg')
    os.remove("img3d.jpg")

