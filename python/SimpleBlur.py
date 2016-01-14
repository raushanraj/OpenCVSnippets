#image processing module

'''import cv2
from cv2 import cv
from GUI import *

def simpleblur(src,dst):
    cv.Smooth(src,dst,cv.CV_BLUR,9,9)
    display(src,"Source Image")
    display(dst,"Simple Smooth")
    cv.WaitKey(0)
    cv.DestroyAllWindows()'''

import cv2
from cv2 import cv
from GUI import *

def simpleblur(src,dst):
    cv.Smooth(src,dst,cv.CV_BLUR,9,9)
    display(src,"Source Image")
    display(dst,"Simple Smooth")
    cv.WaitKey(0)
    cv.DestroyAllWindows()
if __name__=='__main__':
    simpleblur(src_image,dst_image)

