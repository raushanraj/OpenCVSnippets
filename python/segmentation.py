"""
1. Segmentation of a skin region(Skin filter module)
2. src is an image 

"""
import cv2
from cv2 import cv
from GUI import *
from database import *

def resize(src):
    x,y=256,256
    dst=cv2.resize(src,(x,y))
    cv2.imwrite("1_1.jpg",dst)
    dst=cv2.imread("1_1.jpg",1)
    return dst
def segmentation(src):
    img=cv2.cvtColor(src,cv.CV_BGR2YCrCb)
    dst=cv2.inRange(img,(0,133,77),(255,173,127))
    return dst

if __name__=="__main__":
    src=cv2.imread(getpath(),1)
    dst=resize(src)
    dst=segmentation(dst)
   
