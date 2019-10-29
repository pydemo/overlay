import os
import cv2
import numpy as np
bg = r'in\Gergiev_art_helps_putin_to_kill.JPG'
ov = r'in\gergiev_is_war_supporter.JPG'
out = r'out\Gergiev_art_helps_putin_to_kill_gergiev_is_war_supporter.JPG'

assert os.path.isfile(bg)
assert os.path.isfile(ov)
background = cv2.imread(bg)
b_h, b_w, b_ch = background.shape
print(b_h, b_w, b_ch)
                
overlay = cv2.imread(ov)
o_h, o_w, o_ch = overlay.shape
print(o_h, o_w, o_ch)
if 1:
    W = 800
    #oriimg = cv2.imread(filename,cv2.CV_LOAD_IMAGE_COLOR)

    imgScale = W/b_w
    new_b_h,new_b_w = int(b_h*imgScale), int(b_w*imgScale)
    new_background = cv2.resize(background,(new_b_w, new_b_h))
    #cv2.imshow("Show by CV2",new_background)
    #cv2.waitKey(0)
    #cv2.imwrite("resizeimg_new_background.jpg",new_background)
     

if 1:
    W = 350
    #oriimg = cv2.imread(filename,cv2.CV_LOAD_IMAGE_COLOR)

    imgScale = W/o_w
    new_o_h,new_o_w = int(o_h*imgScale), int(o_w*imgScale)
    new_overlay = cv2.resize(overlay,(new_o_w, new_o_h))
    #cv2.imshow("Show by CV2",new_overlay)
    #cv2.waitKey(0)
    #cv2.imwrite("resizeimg_new_overlay.jpg",new_overlay)
    
    
if 1:
    square= np.zeros((new_b_h, new_b_w, b_ch), np.uint8)
    square.fill(255)
    x= new_b_w
    y= new_b_h
    print (new_b_h,new_b_w)
    print (new_o_h,new_o_w)
    offset =0
    broad = {int(y - new_o_h) - offset:int(y)- offset, int(x-new_o_w)- offset:int(x)- offset}
    print(broad)
    
    square[int(y - new_o_h) - offset:int(y)- offset, int(x-new_o_w)- offset:int(x)- offset] = new_overlay
    

if 0:
    cv2.imwrite("resizeimg.jpg",newimg)


if 1: #OVERLAY
    OPACITY = 0.7
    added_image = cv2.addWeighted(new_background,0.6,square,0.4,0)
    cv2.imshow('adjusted', added_image)  
    cv2.waitKey()
    cv2.imwrite(out, added_image)
if 1: #CONTRAST

    alpha = 1.3 # Contrast control (1.0-3.0)
    beta = -75 # Brightness control (0-100)

    adjusted = cv2.convertScaleAbs(added_image, alpha=alpha, beta=beta)

    
    cv2.imshow('adjusted', adjusted)
    
    cv2.waitKey()



                    
                    