'''import cv2.cv
from GUI import *
def laplacian():
    cv.Smooth(src_image,dst_image,cv.CV_GAUSSIAN,9,9)
    dst_img=cv.CreateImage((dst_image.width,dst_image.height),8,1)
    cv.CvtColor(dst_image,dst_img,cv.CV_RGB2GRAY)
    cv.Laplace(dst_img,dst_img,5)
    display(dst_img,"Laplacian")
    cv.WaitKey(0)'''


import cv2.cv
from GUI import *
def laplacian():
    cv.Smooth(src_image,dst_image,cv.CV_GAUSSIAN,9,9)
    dst_img=cv.CreateImage((dst_image.width,dst_image.height),8,1)
    cv.CvtColor(dst_image,dst_img,cv.CV_RGB2GRAY)
    cv.Laplace(dst_img,dst_img,5)
    display(dst_img,"Laplacian")
    cv.WaitKey(0)

if __name__=='__main__':
    laplacian()
