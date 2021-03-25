from PIL import Image, ImageDraw


def  lentil(filename, w, *colors):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)