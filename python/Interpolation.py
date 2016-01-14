#Interpolation
'''def InterPolation_methods():
    dst=cv.CreateImage((2*src_image.width,2*src_image.height),8,3)
    cv.Resize(src_image,dst,cv.CV_INTER_NN)
    display(dst,"Nearest Neighbor Interpolation")
    cv.SaveImage("NN.jpg",dst)
    cv.Resize(src_image,dst,cv.CV_INTER_LINEAR)
    display(dst,"Linear Interpolation")
    cv.SaveImage("LI.jpg",dst)
    cv.Resize(src_image,dst,cv.CV_INTER_AREA)
    display(dst,"Area Interpolation")
    cv.SaveImage("AI.jpg",dst)
    cv.Resize(src_image,dst,cv.CV_INTER_CUBIC)
    display(dst,"Cubic Interpolation")
    cv.SaveImage("CI.jpg",dst)
    cv.WaitKey(0)'''
import cv2
from cv2 import cv
from GUI import *
def InterPolation_methods():
    dst=cv.CreateImage((2*src_image.width,2*src_image.height),8,3)
    cv.Resize(src_image,dst,cv.CV_INTER_NN)
    display(dst,"Nearest Neighbor Interpolation")
    cv.SaveImage("NN.jpg",dst)
    cv.Resize(src_image,dst,cv.CV_INTER_LINEAR)
    display(dst,"Linear Interpolation")
    cv.SaveImage("LI.jpg",dst)
    cv.Resize(src_image,dst,cv.CV_INTER_AREA)
    display(dst,"Area Interpolation")
    cv.SaveImage("AI.jpg",dst)
    cv.Resize(src_image,dst,cv.CV_INTER_CUBIC)
    display(dst,"Cubic Interpolation")
    cv.SaveImage("CI.jpg",dst)
    cv.WaitKey(0)



if __name__=='__main__':
    InterPolation_methods()
    
