import requests
from PIL import Image
import io
import datetime

class PicsumPhotoProvider:

    rootUrl = 'https://picsum.photos'

    def get_daily(self):          

        seed = datetime.date.today()
        url = f"/seed/{seed}/1920/1080"

        print(self.rootUrl + url)
        r = requests.get(self.rootUrl + url)                
        return Image.open(io.BytesIO(r.content))