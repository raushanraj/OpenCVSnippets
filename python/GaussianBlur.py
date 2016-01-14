#image processing module

'''import cv2
from cv2 import cv
from GUI import *

def gaussian(src,dst):
    cv.Smooth(src,dst,cv.CV_GAUSSIAN,9,9)
    display(src,"Source Image")
    display(dst,"Gaussian Smooth")
    cv.WaitKey(0)
    cv.DestroyAllWindows()'''

import cv2
from cv2 import cv
from GUI import *

def gaussian(src,dst):
    cv.Smooth(src,dst,cv.CV_GAUSSIAN,9,9)
    display(src,"Source Image")
    display(dst,"Gaussian Smooth")
    cv.WaitKey(0)
    cv.DestroyAllWindows()
if __name__=='__main__':
    gaussian(src_image,dst_image)

