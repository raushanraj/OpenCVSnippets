'''import cv2
from cv2 import *
from GUI import *
dst=cv.CreateImage((2*src_image.width,2*src_image.height),8,3)
def gaussianpyramid():
    display(src_image,"Source Image")
    cv.PyrUp(src_image,dst,cv.CV_GAUSSIAN_5x5)
    #cv.PyrDown(src_image,dst,cv.CV_GAUSSIAN_5x5)
    display(dst,"Destination Image")
    cv.WaitKey(0)'''

import cv2
from cv2 import *
from GUI import *
dst=cv.CreateImage((2*src_image.width,2*src_image.height),8,3)
def gaussianpyramid():
    display(src_image,"Source Image")
    cv.PyrUp(src_image,dst,cv.CV_GAUSSIAN_5x5)
    display(dst,"Destination Image")
    cv.WaitKey(0)


if __name__=='__main__':
    gaussianpyramid()
