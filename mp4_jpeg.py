import cv2
vidcap = cv2.VideoCapture(r'C:\Users\alex_\OneDrive\Desktop\Gergiev_2_warhol\C0014.MP4')
success,image = vidcap.read()
count = 0
while success:
  a= cv2.imwrite(r"C:\Users\alex_\OneDrive\Desktop\Gergiev_2_warhol\jpegs\frame%d.jpg" % count, image)     # save frame as JPEG file      
  print (a)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1