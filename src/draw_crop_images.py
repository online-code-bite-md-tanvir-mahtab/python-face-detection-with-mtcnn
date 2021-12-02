import os
from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt

class DrawCropedImages:
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
            self.draw_faces(f)

    
    def draw_faces(self,filename):
        data = plt.imread(f"demoreader/results/{filename}")
        for i in range(len(self.result_list)):
            x1,y1,width,height=self.result_list[i]['box']
            x2,y2 = x1 + width, y1 + height
            # defining the plot
            plt.subplot(1,len(self.result_list),i+1)
            plt.axis('off')
            plt.imshow(data[y1:y2,x1:x2])
        plt.show()