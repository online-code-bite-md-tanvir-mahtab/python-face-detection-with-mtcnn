import cv2
from mtcnn import MTCNN
import os
import matplotlib.pyplot as plt

class DrawTheBox:
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
            self.draw_face_box(f)
    
    # creating a function
    # that will detect the face and draw the box sround it
    def draw_face_box(self,filename):
        # loading the image
        data = plt.imread(f"demoreader/results/{filename}")
        plt.imshow(data)
        # creating the boxes
        ax = plt.gca()
        for reuslt in self.result_list:
            x,y,width,height = reuslt['box']
            # now i am going to create the shape
            rect =plt.Rectangle((x,y),width,height,fill=False,color='orange')
            ax.add_patch(rect)
            # to draw the dots
            for key, value in reuslt['keypoints'].items():
                # create and draw dot
                dot = plt.Circle(value, radius=20, color='red')
                ax.add_patch(dot)
        plt.show()