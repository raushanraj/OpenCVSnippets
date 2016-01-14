'''import cv2.cv
from GUI import *
def sobel():
    cv.Smooth(src_image,dst_image,cv.CV_GAUSSIAN,3,3)
    src_gray=cv.CreateImage((src_image.width,src_image.height),8,1)
    dst_gray1=cv.CreateImage((src_image.width,src_image.height),8,1)
    dst_gray=cv.CreateImage((src_image.width,src_image.height),8,1)
    cv.CvtColor(src_image,src_gray,cv.CV_BGR2GRAY)
    cv.Sobel(src_gray,dst_gray1,0,1,3)
    cv.ConvertScaleAbs(dst_gray1,dst_gray1,1,0)
    cv.Sobel(src_gray,dst_gray,1,0,3)
    cv.ConvertScaleAbs(dst_gray,dst_gray,1,0)
    cv.AddWeighted(dst_gray,0.5,dst_gray1,0.5,0,dst_gray)
    cv.NamedWindow("Destination Image")
    cv.ShowImage("Destination Image",dst_gray)
    cv.WaitKey(0)
    
'''

import cv2.cv
from GUI import *
def sobel():
    cv.Smooth(src_image,dst_image,cv.CV_GAUSSIAN,3,3)
    src_gray=cv.CreateImage((src_image.width,src_image.height),8,1)
    dst_gray1=cv.CreateImage((src_image.width,src_image.height),8,1)
    dst_gray=cv.CreateImage((src_image.width,src_image.height),8,1)
    cv.CvtColor(src_image,src_gray,cv.CV_BGR2GRAY)
    cv.Sobel(src_gray,dst_gray1,0,1,3)
    cv.ConvertScaleAbs(dst_gray1,dst_gray1,1,0)
    cv.Sobel(src_gray,dst_gray,1,0,3)
    cv.ConvertScaleAbs(dst_gray,dst_gray,1,0)
    cv.AddWeighted(dst_gray,0.5,dst_gray1,0.5,0,dst_gray)
    cv.NamedWindow("Destination Image")
    cv.ShowImage("Destination Image",dst_gray)
    cv.WaitKey(0)


if __name__=='__main__':
    sobel()
    
