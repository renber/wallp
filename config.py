from py.unsplash import UnsplashPhotoProvider
from py.bing import BingPhotoProvider
from py.picsum import PicsumPhotoProvider
from py.localimg import LocalImageProvider
from py.im_utils import ImageRect

# the supported services
providers = {"unsplash": UnsplashPhotoProvider(), "bing": BingPhotoProvider(), "picsum": PicsumPhotoProvider(), "local": LocalImageProvider()}

# wallpaper arrangement
rects = [
    ImageRect(0, 400, 1920, 1080), 
    ImageRect(1920, 0, 1080, 1920), 
    ImageRect(1920 + 1080, 400, 1920, 1080)
]