import numpy as np
 
from PIL import Image

gscale = '@%#*+=-:. '
 
def getAverageL(image):
    im = np.array(image)

    w,h = im.shape
 
    return np.average(im.reshape(w*h))
 
def covertImageToAscii(fileName, cols, scale):
    global gscale1, gscale2
 
    image = Image.open(fileName).convert('L')

    W, H = image.size[0], image.size[1]

    w = W/cols

    h = w/scale

    rows = int(H/h)

    if cols > W or rows > H:
        exit(0)

    aimg = []

    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        if j == rows-1:
            y2 = H

        aimg.append("")
 
        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)

            if i == cols-1:
                x2 = W

            img = image.crop((x1, y1, x2, y2))

            avg = int(getAverageL(img))

            gsval = gscale[int((avg*9)/255)]

            aimg[j] += gsval

    return aimg


def convert(path, res):   
    imgFile = path
 
    cols = int(res)
    scale = 0.43

    aimg = covertImageToAscii(imgFile, cols, scale)

    out = ""
    for row in aimg:
        out += row + "\n"
    
    return out
