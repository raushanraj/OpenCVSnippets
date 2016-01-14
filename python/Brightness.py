#convert to
'''
from cv2 import cv
from GUI import *
def convertto():
    image=cv.LoadImageM("C:\\Users\\raj\\Desktop\\s4.jpg",cv.CV_LOAD_IMAGE_COLOR)
    newimage=cv.CreateMat(image.rows,image.cols,image.type)
    cv.SetZero(newimage)
    cv.ConvertScale(image,newimage,2.2,50.0)
    display(image,"Source")
    display(newimage,"Destination")
    cv.WaitKey(0)'''
from cv2 import cv
from GUI import *
def convertto():
    image=cv.LoadImageM(getpath(),cv.CV_LOAD_IMAGE_COLOR)
    newimage=cv.CreateMat(image.rows,image.cols,image.type)
    cv.SetZero(newimage)
    cv.ConvertScale(image,newimage,2.2,50.0)
    display(image,"Source")
    display(newimage,"Destination")
    cv.WaitKey(0)


if __name__=='__main__':
    convertto()
