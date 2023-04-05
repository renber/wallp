from PIL import Image

class LocalImageProvider:
     def get_daily(self):          
        return Image.open("wallpaper.jpg")