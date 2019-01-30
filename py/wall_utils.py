import os
import ctypes

def set_wallpaper(path):
    '''
    Sets the current desktop wallpaper to the file at the specified path

    Currently only Windows is supported
    '''
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(path), 0)