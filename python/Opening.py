'''import cv2
from cv2 import cv
from GUI import *
def opening():
    display(src_image,"source_image")
    cv.WaitKey(0)
    struc=cv.CreateStructuringElementEx(5,5,3,3,cv.CV_SHAPE_RECT)
    dst=cv.CreateImage((src_image.width,src_image.height),8,src_image.channels)
    temp=cv.CreateImage((src_image.width,src_image.height),8,src_image.channels)
    cv.MorphologyEx(src_image,dst,temp,struc,cv2.MORPH_OPEN,1)
    display(dst,"destination image")
    cv.WaitKey(0)
    cv.DestroyAllWindows()'''

import cv2
from cv2 import cv
from GUI import *
def opening():
    display(src_image,"source_image")
    struc=cv.CreateStructuringElementEx(5,5,3,3,cv.CV_SHAPE_RECT)
    dst=cv.CreateImage((src_image.width,src_image.height),8,src_image.channels)
    temp=cv.CreateImage((src_image.width,src_image.height),8,src_image.channels)
    cv.MorphologyEx(src_image,dst,temp,struc,cv2.MORPH_OPEN,1)
    display(dst,"destination image")
    cv.WaitKey(0)
    cv.DestroyAllWindows()

if __name__=='__main__':
    opening()

