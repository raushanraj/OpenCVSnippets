#image processing module

'''import cv2
from cv2 import cv
from GUI import *

def Bilateral(src,dst):
    cv.Smooth(src,dst,cv.CV_BILATERAL,9,9)
    display(src,"Source Image")
    display(dst,"Bilateral Smooth")
    cv.WaitKey(0)
    cv.DestroyAllWindows()'''

import cv2
from cv2 import cv
from GUI import *

def Bilateral(src,dst):
    cv.Smooth(src,dst,cv.CV_BILATERAL,9,9)
    display(src,"Source Image")
    display(dst,"Bilateral Smooth")
    cv.WaitKey(0)
    cv.DestroyAllWindows()
if __name__=='__main__':
    Bilateral(src_image,dst_image)

