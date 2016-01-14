#resize the image
'''import cv2.cv
from GUI import *
def resize():
    original=cv.LoadImageM("C:\\Users\\raj\\Desktop\\s4.jpg")
    thumbnail=cv.CreateMat(original.rows/10,original.cols/10,cv2.cv.CV_8UC3)
    cv.Resize(original,thumbnail)
    cv.NamedWindow("destination",1)
    cv.ShowImage("destination",thumbnail)
    cv.WaitKey(0)
'''
import cv2.cv
from GUI import *
from database import *
def resize():
    original=cv.LoadImageM(getpath())
    thumbnail=cv.CreateMat(original.rows/10,original.cols/10,cv2.cv.CV_8UC3)
    cv.Resize(original,thumbnail)
    cv.NamedWindow("destination",1)
    cv.ShowImage("destination",thumbnail)
    cv.WaitKey(0)
if __name__=='__main__':
    resize()

