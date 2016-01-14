import cv2
from cv2 import cv
from database import *

src_image=cv.LoadImageM(getpath(),cv.CV_LOAD_IMAGE_COLOR)
dst_image=cv.CreateImage((src_image.width,src_image.height),8,src_image.channels)
cv.SetZero(dst_image)
#src_image=cv.LoadImageM("C:\\Users\\raj\\Desktop\\image processing and computer vision\\pictures\\s4.jpg")
def display(img,name):
    cv.NamedWindow(name,1)
    cv.ShowImage(name,img)
    

