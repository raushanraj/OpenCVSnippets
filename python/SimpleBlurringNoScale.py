#image processing module

'''import cv2
from cv2 import cv
from GUI import *

def simpleblurnoscale(src,dst):
    cv.Smooth(src,dst,cv.CV_BLUR,9,9)
   display(src,"Source Image")
    display(dst,"Simple No Scale Smoothing")
    cv.WaitKey(0)
    cv.DestroyAllWindows()'''

import cv2
from cv2 import cv
from GUI import *

def simpleblurnoscale(src,dst):
    cv.Smooth(src,dst,cv.CV_BLUR,9,9)
    display(src,"Source Image")
    display(dst,"Simple No Scale Smoothing")
    cv.WaitKey(0)
    cv.DestroyAllWindows()
if __name__=='__main__':
    simpleblurnoscale(src_image,dst_image)

