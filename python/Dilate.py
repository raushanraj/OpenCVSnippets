'''import cv2
from cv2 import cv
from GUI import *
def dilationofimage():
    display(src_image,"Source Image")
    struc=cv.CreateStructuringElementEx(50,50,25,25,cv.CV_SHAPE_RECT)
    cv.Dilate(src_image,dst_image,struc,1)
    display(dst_image,"Dilation")
    cv.WaitKey(0)
    cv.DestroyWindow("Dilation")'''

import cv2
from cv2 import cv
from GUI import *
def dilationofimage():
    display(src_image,"Source Image")
    struc=cv.CreateStructuringElementEx(10,10,5,5,cv.CV_SHAPE_RECT)
    cv.Dilate(src_image,dst_image,struc,1)
    display(dst_image,"Dilation")
    cv.WaitKey(0)
    cv.DestroyWindow("Dilation")

if __name__=='__main__':
    dilationofimage()
