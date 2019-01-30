from py.unsplash import *
from py.bing import *
from py.im_utils import *

# the supported services
providers = {"unsplash": UnsplashPhotoProvider(), "bing": BingPhotoProvider()}

# wallpaper arrangement
rects = [ImageRect(0, 0, 1920, 1080)]