'''import cv2
from cv2 import cv
from GUI import *
def floodfill():
    display(src_image,"source_image")
    seedPoint=(0,0)
    cv.FloodFill(src_image,seedPoint,(0,255,0),(2,10,50),(2,10,50),4,None)
    display(src_image,"Destination image")
    cv.WaitKey(0)'''

import cv2
from cv2 import cv
from GUI import *
def floodfill():
    display(src_image,"source_image")
    seedPoint=(0,0)
    cv.FloodFill(src_image,seedPoint,(0,255,0),(2,10,50),(2,10,50),4,None)
    display(src_image,"Destination image")
    cv.WaitKey(0)
    
if __name__=='__main__':
    floodfill() 
