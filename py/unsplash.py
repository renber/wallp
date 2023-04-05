import requests
from PIL import Image
import io
import datetime

class UnsplashPhotoProvider:

    #rootUrl = 'https://source.unsplash.com/1920x1080/?pic-of-the-day'
    rootUrl = 'https://source.unsplash.com/random/1920x1080'

    def get_daily(self):          
        #seed = datetime.date.today()
        url = f"{self.rootUrl}"
        print(url)
        r = requests.get(url) 
        return Image.open(io.BytesIO(r.content))