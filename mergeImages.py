import numpy as np
from PIL import Image
from os import listdir
import os
from os.path import isfile, join
size = 1920, 1080
def resize_all():
    image_path = r"C:\Users\G603344\Desktop\personal\swapbackground\images"
    onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]
    for x in range(0, len(onlyfiles)):
        my_image = "\\".join([image_path, onlyfiles[x]])
        im = Image.open(my_image).convert('RGB')
        im = im.resize(size, Image.ANTIALIAS)
        im.save("images\\" + onlyfiles[x].split(".")[0] + ".jpg")
        print("Done")
        if(not(onlyfiles[x].split(".")[1]=="jpg")):
            os.remove(my_image)
            print(onlyfiles[x])
            print("deleted")
    print("All Images resized")

def merge_image():
    image_path = r"C:\Users\G603344\Desktop\personal\swapbackground\images"
    onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]
    for x in range(0, len(onlyfiles), 2):
        print(x)
        my_image = "\\".join([image_path, onlyfiles[x]])
        if(x==76):
         my_image1 = "\\".join([image_path, onlyfiles[0]])
        else:
         my_image1 = "\\".join([image_path, onlyfiles[x+1]])
        list_im = [my_image,my_image1]
        imgs    = [ Image.open(i) for i in list_im ]
        imgs_comb = np.hstack((np.asarray(i) for i in imgs ))
        imgs_comb = Image.fromarray(imgs_comb)
        imgs_comb.save( "imagesDoubleScreen\\"+onlyfiles[x].split('.')[0]+'.jpg' )


if __name__ == "__main__":
    resize_all()
    merge_image()
    print("Done")

