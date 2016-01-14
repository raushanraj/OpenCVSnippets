'''#median filtering
import cv2
from cv2 import cv
k="C:\\Users\\raj\\Desktop\\sa1.png"

def medianfiltering():
    src=cv.LoadImageM(k,cv.CV_LOAD_IMAGE_COLOR)
    dst=cv.CreateImage((src.width,src.height),8,src.channels)
    cv.SetZero(dst)
    cv.NamedWindow("Median Filtering",1)
    cv.NamedWindow("After Filtering",1)
    cv.Smooth(src,dst,cv.CV_MEDIAN,9,9)
    cv.ShowImage("Median Filtering",src)
    cv.ShowImage("After Filtering",dst)
    cv.WaitKey(0)'''

#median filtering
import cv2
from cv2 import cv
from database import *
k=getpath()

def medianfiltering():
    src=cv.LoadImageM(k,cv.CV_LOAD_IMAGE_COLOR)
    dst=cv.CreateImage((src.width,src.height),8,src.channels)
    cv.SetZero(dst)
    cv.NamedWindow("Median Filtering",1)
    cv.NamedWindow("After Filtering",1)
    cv.Smooth(src,dst,cv.CV_MEDIAN,9,9)
    cv.ShowImage("Median Filtering",src)
    cv.ShowImage("After Filtering",dst)
    cv.WaitKey(0)
    
if __name__=='__main__':
    medianfiltering()
