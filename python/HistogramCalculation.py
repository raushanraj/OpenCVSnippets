'''import cv2
from cv2 import cv
from GUI import *
import numpy as np


def calculatehistogram():
    src=cv2.imread("C:\\Users\\raj\\Desktop\\s4.jpg",cv.CV_LOAD_IMAGE_COLOR)
    b,g,r=cv2.split(src)
    h=np.zeros((300,255,3))
    color = [ (255,0,0),(0,255,0),(0,0,255) ]
    bins=np.arange(256).reshape(256,1)
    for plane,color in zip([b,g,r],color):
        hist_plane=cv2.calcHist([plane],[0],None,[256],[0,255])
        cv2.normalize(hist_plane,hist_plane,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.round(hist_plane))
        pts=np.column_stack((bins,hist))
        cv2.polylines(h,[pts],False,color)
    h=np.flipud(h)
    cv2.imshow("histogram",h)
    cv.WaitKey(0)'''

import cv2
from cv2 import cv
from GUI import *
import numpy as np
from database import *


def calculatehistogram():
    src=cv2.imread(getpath(),cv.CV_LOAD_IMAGE_COLOR)
    b,g,r=cv2.split(src)
    h=np.zeros((300,255,3))
    color = [ (255,0,0),(0,255,0),(0,0,255) ]
    bins=np.arange(256).reshape(256,1)
    for plane,color in zip([b,g,r],color):
        hist_plane=cv2.calcHist([plane],[0],None,[256],[0,255])
        cv2.normalize(hist_plane,hist_plane,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.round(hist_plane))
        pts=np.column_stack((bins,hist))
        cv2.polylines(h,[pts],False,color)
    h=np.flipud(h)
    cv2.imshow("histogram",h)
    cv.WaitKey(0)
if __name__=='__main__':
    calculatehistogram()
