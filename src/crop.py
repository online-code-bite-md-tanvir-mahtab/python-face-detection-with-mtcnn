# creating the Crop class
import os
from mtcnn import MTCNN
import cv2

class CropImage:
    def __init__(self,source_dir,dest_dir,mode):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.mode = mode
        self.crop_image()

    def crop_image(self):
        # creaing the diractory if dosen't exist
        if os.path.isdir(self.dest_dir)==False:
            os.mkdir(self.dest_dir)
        detector = MTCNN()
        source_list=os.listdir(self.source_dir)
        uncropped_file_list=[]
        for f in source_list:
            f_path=os.path.join(self.source_dir, f)
            dest_path=os.path.join(self.dest_dir,f)
            img=cv2.imread(f_path)
            data=detector.detect_faces(img)
            if data ==[]:
                uncropped_file_list.append(f_path)
            else:
                if self.mode==1:  #detect the box with the largest area
                    for i, faces in enumerate(data): # iterate through all the faces found
                        box=faces['box']  # get the box for each face                
                        biggest=0                    
                        area = box[3]  * box[2]
                        if area>biggest:
                            biggest=area
                            bbox=box 
                    bbox[0]= 0 if bbox[0]<0 else bbox[0]
                    bbox[1]= 0 if bbox[1]<0 else bbox[1]
                    img=img[bbox[1]: bbox[1]+bbox[3],bbox[0]: bbox[0]+ bbox[2]] 
                    cv2.imwrite(dest_path, img)
                else:
                    for i, faces in enumerate(data): # iterate through all the faces found
                        box=faces['box']
                        if box !=[]:
                            # return all faces found in the image
                            box[0]= 0 if box[0]<0 else box[0]
                            box[1]= 0 if box[1]<0 else box[1]
                            cropped_img=img[box[1]: box[1]+box[3],box[0]: box[0]+ box[2]]
                            fname=os.path.splitext(f)[0]
                            fext=os.path.splitext(f)[1]
                            fname=fname + str(i) + fext
                            save_path=os.path.join(dest_dir,fname )
                            cv2.imwrite(save_path, cropped_img)  
        for f in uncropped_file_list:
            print(f)
