import requests
from lxml import etree
from PIL import Image
import io

class BingPhotoProvider:

    region = "de-DE"
    rootUrl = 'http://www.bing.com/'
    dailyUrl = rootUrl + 'HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=' + region

    def get_daily(self):

        print("Requesting Photo Of The Day from bing.com")
        r = requests.get(self.dailyUrl)
        # an xml file is returned
        tree = etree.fromstring(r.content)

        linkTag = tree.xpath('//urlBase');
        if len(linkTag) > 0:
            photoPage = linkTag[0].text
            print("Downloading image")
            r = requests.get(self.rootUrl + photoPage + "_1920x1080.jpg")
            return Image.open(io.BytesIO(r.content))

        return None