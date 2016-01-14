'''import cv2
from cv2 import cv
import numpy as np


def histogramequalization():
    src=cv.LoadImage("C:\\Users\\raj\\Desktop\\s4.jpg",cv.CV_LOAD_IMAGE_GRAYSCALE)
    dst=cv.CreateImage((src.width,src.height),src.depth,src.channels)
    cv.EqualizeHist(src,dst)
    cv.NamedWindow("SourceImage",1)
    cv.NamedWindow("EqualizedImage",1)
    cv.ShowImage("SourceImage",src)
    cv.ShowImage("EqualizedImage",dst)
    cv.WaitKey(0)'''


import cv2
from cv2 import cv
import numpy as np
from database import *

def histogramequalization():
    src=cv.LoadImage(getpath(),cv.CV_LOAD_IMAGE_GRAYSCALE)
    dst=cv.CreateImage((src.width,src.height),src.depth,src.channels)
    cv.EqualizeHist(src,dst)
    cv.NamedWindow("SourceImage",1)
    cv.NamedWindow("EqualizedImage",1)
    cv.ShowImage("SourceImage",src)
    cv.ShowImage("EqualizedImage",dst)
    cv.WaitKey(0)

if __name__=='__main__':
    histogramequalization()
