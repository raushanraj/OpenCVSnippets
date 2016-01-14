'''import cv2.cv
from GUI import *
import numpy as np


def HoughLineSegmentTransform():
    im=cv2.imread("C:\\Users\\raj\\Desktop\\s4.png")
    gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray_im,(3,3),0)
    edges=cv2.Canny(blur,150,200,3)
    m,n=gray_im.shape
    img=im.copy()
    lines=cv2.HoughLinesP(edges,1,np.pi/180,12)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.namedWindow("show")
    cv2.imshow("show",img)
    cv2.waitKey(0)'''
import cv2.cv
from GUI import *
import numpy as np
from database import *


def HoughLineSegmentTransform():
    im=cv2.imread(getpath())
    gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray_im,(3,3),0)
    edges=cv2.Canny(blur,150,200,3)
    m,n=gray_im.shape
    img=im.copy()
    lines=cv2.HoughLinesP(edges,1,np.pi/180,12)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.namedWindow("show")
    cv2.imshow("show",img)
    cv2.waitKey(0)

if __name__=='__main__':
    HoughLineSegmentTransform()
