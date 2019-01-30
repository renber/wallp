# wallp
Python script to download pictures from online services (e.g. unsplash, bing) and set them as wallpaper (currently Windows only).

## Usage
Run `python wallp.py unsplash` or `python wallp.py bing` to download the photo of the day from unsplash.com or bing.com, respectively and set it as desktop wallpaper.

## Configuration

By default _wallp_ creates a wallpaper with size 1920x1080 by scaling the downloaded image. Depending on your screen resolution or layout (multiple monitors etc.) you may want to adjust the outputted wallpaper.
You can do this in ´config.py´. Currently this file contains the following options:

### providers
List of photo provider keywords and implementation class (currently unsplash and bing). Add new provider implementations here for them to be available.
For instance: ´providers = {"unsplash": UnsplashPhotoProvider(), "bing": BingPhotoProvider()}´

### rects
Definition of the wallpaper layout.
An enumeration of ImageRect values which each define a location (x,y) and size(width,height) where the downloaded image should be put on the wallpaper. That means, having multiple ImageRect entries here will put the photo multiple times on the wallpaper. For that the image is resized to each ImageRect's size individually while its aspect ratio is kept, if the target area is too small to hold the resized image it is centered in the area and cropped.
This allows to easily define monitor overlapping images in multi-monitor environments.

Default value: `rects = [ImageRect(0, 420, 1920, 1080)]`
Multi-monitor example:
Imagine you have three Full-HD monitors which are arranged like this (the first one has a horizontal orientation the other two are placed  vertically rotated to the right):
´´´
                   |--------||--------|
|-----------------||        ||        |
|       1         ||   2    ||   3    |
|                 ||        ||        |
|-----------------||        ||        |
                   |--------||--------|
´´´
Using the definition ´rects = [ImageRect(0, 420, 1920, 1080), ImageRect(1920, 0, 2160, 1920)]´ will place th ephoto scaled on monitor 1 and a second scaled version on monitor 2 and 3 seamlessly.

Note: The created wallpaper image always has the size to exactly hold the image rects (i.e. maximum horizontal and vertical extent from the rects definition). In the sample case this would be 4080x1920 pixels.
