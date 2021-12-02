# now i am going to import the mtcnn library
from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt
import pandas 
import numpy as np
from crop import *
import os
from draw_crop_images import *
from draw import *
from draw_graph import *

# this method i have created to check how many data we can gather
# as a dectionaries 
def test_data(faces):
    for pepole in faces:
        left_eye = pepole['keypoints']['left_eye']
        right_eye = pepole['keypoints']['right_eye']
        nose = pepole['keypoints']['nose']
        mouth_left = pepole['keypoints']['mouth_left']
        mouth_right = pepole['keypoints']['mouth_right']
        # nwo i want show the data ss 
        print(f"the eye :{left_eye},{right_eye} the nose :{nose} the mouth :{mouth_left},{mouth_right}")
        # print(pepole)






if __name__ == '__main__':
    source_dir = 'demoreader/images'
    dest_dir = 'demoreader/results'

    # we are creating the object of the CropImage class
    cropImage = CropImage(source_dir,dest_dir,1)
    print(cropImage)
    drawImage = DrawCropedImages(dest_dir)
    print(drawImage)
    box = DrawTheBox(dest_dir)
    print(box)
    graph = Graph(dest_dir)
    print(graph)
    drawImage = DrawCropedImages(dest_dir)
    print(drawImage)
    
 


