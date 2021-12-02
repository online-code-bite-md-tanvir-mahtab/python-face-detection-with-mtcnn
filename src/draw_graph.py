import cv2
from mtcnn import MTCNN
import os
import matplotlib.pyplot as plt
# creating the constant
X_AXIS = ['left_eye','right_eye','nose','mouth_right','mouth_left']
Y_AXIS = []
class Graph:
    def __init__(self,dest_dir):
        self.dest_dir = dest_dir
        detector = MTCNN()
        self.cropted_list = os.listdir(self.dest_dir)
        # detecting the faces from the file
        for f in self.cropted_list:
            f_path = os.path.join(self.dest_dir,f)
            # now i am giong to read the image
            img = cv2.imread(f_path)
            # now i aam going to detact the face
            self.result_list = detector.detect_faces(img)
            for faces in self.result_list:
                self.design_the_graph(faces)
    
    def design_the_graph(self,faces):
        plt.title("face detaction")
        plt.ylabel("Acuracy ")
        plt.xlabel("Parts of face")
        left_eye = faces['keypoints']['left_eye'][0]
        right_eye = faces['keypoints']['right_eye'][0]
        nose = faces['keypoints']['nose'][0]
        mouth_left = faces['keypoints']['mouth_left'][0]
        mouth_right = faces['keypoints']['mouth_right'][0]
        Y_AXIS.append(left_eye%100)
        Y_AXIS.append(right_eye%100)
        Y_AXIS.append(nose%100)
        Y_AXIS.append(mouth_right%100)
        Y_AXIS.append(mouth_left%100)
        plt.bar(X_AXIS,Y_AXIS)
        plt.show()