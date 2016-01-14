'''import cv2.cv
from GUI import *
import numpy as np


def Houghcircle():
    imc=cv2.imread("circle.png")
    im=cv2.imread("circle.png",0)
    im_blur=cv2.GaussianBlur(im,(3,3),0)
    img=im.copy()
    circles=cv2.HoughCircles(im_blur,cv.CV_HOUGH_GRADIENT,1,20,param1=60,param2=50)
    print circles
    for circle in circles[0]:
        cv2.circle(imc,(circle[0],circle[1]),circle[2],(0,0,255),1)
        cv2.circle(imc,(circle[0],circle[1]),0,(0,0,255),3)
    cv2.namedWindow("show")
    cv2.imshow("show",imc)
    cv2.waitKey(0)'''

import cv2.cv
from GUI import *
import numpy as np
from database import *


def Houghcircle():
    imc=cv2.imread(getpath())
    im=cv2.imread(getpath(),0)
    im_blur=cv2.GaussianBlur(im,(3,3),0)
    img=im.copy()
    circles=cv2.HoughCircles(im_blur,cv.CV_HOUGH_GRADIENT,1,20,param1=60,param2=50)
    print circles
    for circle in circles[0]:
        cv2.circle(imc,(circle[0],circle[1]),circle[2],(0,0,255),1)
        cv2.circle(imc,(circle[0],circle[1]),0,(0,0,255),3)
    cv2.namedWindow("show")
    cv2.imshow("show",imc)
    cv2.waitKey(0)
    

if __name__=='__main__':
    Houghcircle()

        
