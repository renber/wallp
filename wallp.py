from PIL import Image
import time
from py.opts import *
from py.im_utils import *
from py.wall_utils import *
import config

def main():

    opt = getCommandLineOptions()

    rects = config.rects

    # get required bounds for the wallpaper image
    targetWidth = max(rects, key=lambda r: r.x + r.width)
    targetWidth = targetWidth.x + targetWidth.width
    targetHeight = max(rects, key=lambda r: r.y + r.height)
    targetHeight = targetHeight.y + targetHeight.height    
    
    # read photo of the day link
    provider = config.providers[opt.provider]    

    photo = provider.get_daily()

    if photo is None:
        print("No file could be downloaded")
        return

    print("Arranging image")
    img = Image.new('RGB', (targetWidth, targetHeight), color = 'white')

    for r in rects:            
        resizedPhoto = resize_keep_aspect(photo, r.width, r.height, Image.LANCZOS )
        img.paste(resizedPhoto, (r.x, r.y))
    
    print("Setting Wallpaper")
    img.save("wall.jpg", "JPEG")
    set_wallpaper("wall.jpg")    

if __name__ == '__main__':
    main()
