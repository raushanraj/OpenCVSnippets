'''
from cv2 import cv
from GUI import *
def adaptivethreshold():
    cv.AdaptiveThreshold(src,dst,255,cv.CV_ADAPTIVE_THRESH_MEAN_C,cv.CV_THRESH_BINARY_INV,3,5)
    display(dst,"Destination Image")
    cv.WaitKey(0)
'''

from cv2 import cv
from GUI import *
from database import *
path=getpath()
src=cv.LoadImage(path,0)
dst=cv.CreateImage((src.width,src.height),8,src.channels);

def adaptivethreshold():
    display(src,"Source Image")
    cv.AdaptiveThreshold(src,dst,255,cv.CV_ADAPTIVE_THRESH_MEAN_C,cv.CV_THRESH_BINARY_INV,3,5)
    display(dst,"Destination Image")
    cv.WaitKey(0)

if __name__=='__main__':
    adaptivethreshold()
