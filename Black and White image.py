from PIL import Image


def bw_convert():
    nkar = Image.open("image.jpg")
    pixelner = nkar.load()
    x, y = nkar.size
    for i in range(x):
        for j in range(y):
            r = pixelner[i, j][0]
            g = pixelner[i, j][1]
            b = pixelner[i, j][2]
            c = (0.2989 * r) + (0.5870 * g) + (0.1140 * b)
            c = round(c)
            pixelner[i, j] = c, c, c
    nkar.save("res.jpg")