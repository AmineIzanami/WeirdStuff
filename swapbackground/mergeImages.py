import numpy as np
from PIL import Image
from os import listdir
import os
from os.path import isfile, join
size = 1920, 1080
new_ones=0

def resize_all():
    global new_ones
    image_path = r"C:\Users\G603344\Desktop\personal\swapbackground\images"
    onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]
    for x in range(0, len(onlyfiles)):
        my_image = "\\".join([image_path, onlyfiles[x]])
        im = Image.open(my_image).convert('RGB')
        if(not(onlyfiles[x].split(".")[1] == "jpg" and im.size==size)):
            im = im.resize(size, Image.ANTIALIAS)
            im.save("images\\" + onlyfiles[x].split(".")[0] + ".jpg")
            print(onlyfiles[x].split(".")[0] + ".jpg Done")
            if(not(onlyfiles[x].split(".")[1]=="jpg")):
                os.remove(my_image)
                print(onlyfiles[x])
                print("deleted")
            new_ones = new_ones + 1
        else:
            print(onlyfiles[x].split(".")[0] + ".jpg is already done")
    print("All Images resized")

def merge_image():
    from pathlib import Path
    global new_ones
    image_path = r"C:\Users\G603344\Desktop\personal\swapbackground\images"
    onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]
    for x in range(0, len(onlyfiles), 2):
        my_file = Path("imagesDoubleScreen\\"+onlyfiles[x].split('.')[0]+'.jpg' )
        if not my_file.exists():
            print(x)
            my_image = "\\".join([image_path, onlyfiles[x]])
            if(x==len(onlyfiles)):
             my_image1 = "\\".join([image_path, onlyfiles[0]])
            else:
             my_image1 = "\\".join([image_path, onlyfiles[x+1]])
            list_im = [my_image,my_image1]
            imgs    = [ Image.open(i) for i in list_im ]
            imgs_comb = np.hstack((np.asarray(i) for i in imgs ))
            imgs_comb = Image.fromarray(imgs_comb)
            imgs_comb.save( "imagesDoubleScreen\\"+onlyfiles[x].split('.')[0]+'.jpg' )
            new_ones = new_ones + 1
        else:
            print(my_file.name+"Already exist")


def downlaod_new():
    from google_images_download import google_images_download
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":"Motivation quote","limit":100,"size": "large","print_urls":True,"no_numbering":1}
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images

if __name__ == "__main__":
    resize_all()
    merge_image()
    print("Done     image processed : "+str(new_ones))

