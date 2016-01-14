'''#canny edge detector
import cv2.cv
from GUI import *

def canny_edge_detector():
    cv.Smooth(src_image,dst_image,cv.CV_GAUSSIAN,5,5)
    dst_gray=cv.CreateImage((dst_image.width,dst_image.height),8,1)
    cv.CvtColor(dst_image,dst_gray,cv.CV_BGR2GRAY)
    cv.Canny(dst_gray,dst_gray,50,150,3)
    cv.Threshold(dst_gray,dst_gray,0,255,0)
    cv.CvtColor(dst_gray,dst_image,cv.CV_GRAY2BGR)
    cv.Add(dst_image,src_image,src_image)
    display(src_image,"Canny Edge Detected")
    cv.WaitKey(0)


import cv2.cv
import numpy as np
from GUI import *

def CannyThreshold():
    img=cv2.imread("s4.png")
    gray_im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    smooth=cv2.GaussianBlur(gray_im,(3,3),0)
    smooth=cv2.Canny(smooth,10,30,3)
    cv2.namedWindow("Canny Thresholding")
    cv2.imshow("Canny Thresholding",smooth)
    cv2.waitKey(0)


    '''

#canny edge detector
import cv2.cv
import numpy as np
from GUI import *
from database import *

def CannyThreshold():
    img=cv2.imread(getpath())
    gray_im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    smooth=cv2.GaussianBlur(gray_im,(3,3),0)
    smooth=cv2.Canny(smooth,10,30,3)
    cv2.namedWindow("Canny Thresholding")
    cv2.imshow("Canny Thresholding",smooth)
    cv2.waitKey(0)
    
if __name__=='__main__':
    CannyThreshold()
    



