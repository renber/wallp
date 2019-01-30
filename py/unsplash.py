import requests
from lxml import html
from PIL import Image
import io

class UnsplashPhotoProvider:

    rootUrl = 'https://www.unsplash.com'

    def get_daily(self):

        print("Requesting Photo Of The Day from unsplash.com")
        r = requests.get(self.rootUrl)
        tree = html.fromstring(r.content)

        linkTag = tree.xpath('//a[text()="Photo of the Day"]');
        if len(linkTag) > 0:
            photoPage = linkTag[0].attrib['href']
            print("Downloading image")
            r = requests.get(self.rootUrl + photoPage + '/download?force=true')        
            return Image.open(io.BytesIO(r.content))

        return None