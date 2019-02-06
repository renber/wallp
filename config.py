from py.unsplash import *
from py.bing import *
from py.im_utils import *

# the supported services
providers = {"unsplash": UnsplashPhotoProvider(), "bing": BingPhotoProvider()}

# wallpaper arrangement
rects = [ImageRect(0, 420, 1920, 1080), ImageRect(1920, 0, 2160, 1920)]