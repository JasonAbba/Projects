# program to augment dataset of leave images

import cv2
import numpy as np
from skimage.io import imread_collection

dataset = 'dataset/*.JPG' # path for leaf images

List = imread_collection(dataset)
images_list = np.array(List)
# print(images_list)


def img_augment(images_list):
    img_id = 0 # 0 becomes 1 when it enters for-loop
    for i in np.nditer(images_list):
        folder = 'augmented_dataset/' # destination folder
        ext = '.JPG' # default extension
        img_id += 1 # increments the value
        img = i
        img = cv2.resize(img, (600, 600))

        # horizontal flipping
        horizontal_flip = cv2.flip(img, 0)
        # cv2.imshow('hor img', horizontal_flip)
        name = str(img_id) + '_horizontalflip' 
        filename = name.join([folder, ext])
        cv2.imwrite(filename, horizontal_flip)

        # vertical flipping
        vertical_flip = cv2.flip(img, 1)
        name = str(img_id) + '_verticalflip' 
        filename = name.join([folder, ext])
        cv2.imwrite(filename, vertical_flip)

        # mirroring
        mirror = cv2.flip(img, -1)
        name = str(img_id) + '_mirrored' 
        filename = name.join([folder, ext])
        cv2.imwrite(filename, mirror)

        # blurring
        ksize = (9,9) # kernel lets you define the intensity of blur
        blur = cv2.blur(img, ksize)
        name = str(img_id) + '_blurred' 
        filename = name.join([folder, ext])
        cv2.imwrite(filename, blur)

img_augment(images_list)