import os
import ctypes
from ctypes import wintypes
import random


def set_background():
    image_path = r"C:\Users\G603344\Desktop\personal\swapbackground\imagesDoubleScreen"
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]
    my_image = "\\".join([image_path,onlyfiles[random.randint(1,len(onlyfiles)-1)]])
    ctypes.windll.user32.SystemParametersInfoW(20, 0, my_image, 0)



if __name__ == "__main__":
    set_background()
