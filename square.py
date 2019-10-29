import os, sys, cv2
import numpy as np

import numpy as np
import cv2

e=sys.exit


img = cv2.imread('foo.jpg')



in_img = r'C:\Users\alex_\OneDrive\Pictures\Sony7rM4\SB_Matsuev_20_2019\1-14-2019\insta\DSC00423.JPG'
out_img = in_img.strip('.JPG')+'_2.JPG'


if 1:
        img = cv2.imread(in_img)

        
        #get size
        height, width, channels = img.shape
        if height> width:
            # Create a black image
            x = height if height > width else width
            y = height if height > width else width
            square= np.zeros((x,y,3), np.uint8)
            #
            #This does the job
            #
            square[int((y-height)/2):int(y-(y-height)/2), int((x-width)/2):int(x-(x-width)/2)] = img
            
            #cv2.imshow("original", img)
            #cv2.imshow("black square", square)
            #cv2.waitKey(0)
            cv2.imwrite(out_img,square)
            del img
            os.remove(in_img)
        
        