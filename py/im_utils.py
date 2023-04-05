from PIL import Image
from collections import namedtuple

class ImageRect:

    def __init__(self, x, y, width, height, provider = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.provider = provider

def resize_keep_aspect(img, targetWidth, targetHeight, qualitiy):
    '''
    Resizes img to targetWidth x targetHeight and keeps its aspect ratio
    Resized image is to large for the target area it is centered and cropped accordingly
    '''
    scalingY = img.height / targetHeight;
    scalingX = img.width / targetWidth;
    if scalingX < scalingY:
        scaling = scalingX
    else:
        scaling = scalingY

    newWidth = img.width / scaling;
    newHeight = img.height / scaling;

    if newWidth < targetWidth:
        newWidth = targetWidth
    if newHeight < targetHeight:
        newHeight = targetHeight;

    if newWidth > targetWidth:
        shiftX = int((newWidth - targetWidth) / 2)
    else:
        shiftX = 0

    if newHeight > targetHeight:
        shiftY = int((newHeight - targetHeight) / 2)
    else:
        shiftY = 0

    target = Image.new('RGB', (targetWidth, targetHeight), color = 'white')
    resized = img.resize( (int(newWidth), int(newHeight) ), qualitiy )

    target.paste(resized, (-shiftX, -shiftY) )
    return target