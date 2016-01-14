#HoughTransform
'''import cv2.cv
from GUI import *
import numpy as np

def HoughTransform():
    im=cv2.imread("C:\\Users\\raj\\Desktop\\s4.png")
    gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray_im,(3,3),0)
    edges=cv2.Canny(blur,150,200,3)
    m,n=gray_im.shape
    img=im.copy()
    lines=cv2.HoughLines(edges,1,np.pi/180,60)
    for r,thetha in lines[0]:
        a=np.cos(thetha)
        b=np.sin(thetha)
        x0=a*r
        y0=b*r
        x1 = int(x0 + 1000*(-b)) 
        y1 = int(y0 + 1000*(a)) 
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.namedWindow("show")
    cv2.imshow("show",img)
    cv2.waitKey(0)
HoughTransform()
'''
import cv2.cv
from GUI import *
import numpy as np
from database import *

def HoughTransform():
    im=cv2.imread(getpath())
    gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray_im,(3,3),0)
    edges=cv2.Canny(blur,150,200,3)
    m,n=gray_im.shape
    img=im.copy()
    lines=cv2.HoughLines(edges,1,np.pi/180,60)
    for r,thetha in lines[0]:
        a=np.cos(thetha)
        b=np.sin(thetha)
        x0=a*r
        y0=b*r
        x1 = int(x0 + 100*(-b)) 
        y1 = int(y0 + 100*(a)) 
        x2 = int(x0 - 100*(-b))
        y2 = int(y0 - 100*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.namedWindow("show")
    cv2.imshow("show",img)
    cv2.waitKey(0)

if __name__=='__main__':
    HoughTransform()
