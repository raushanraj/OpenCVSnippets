'''from cv2 import cv
from GUI import *

src=cv.LoadImage("C:\\Users\\raj\\Desktop\\s4.png",0)
dst=cv.CreateImage((src.width,src.height),8,src.channels);
def thresholding():
    cv.Threshold(src,dst,150,255,0)
    display(dst,"Destination Image")
    cv.WaitKey(0)'''

from cv2 import cv
from GUI import *
from database import *

src=cv.LoadImage(getpath(),0)
dst=cv.CreateImage((src.width,src.height),8,src.channels);
def thresholding():
    cv.Threshold(src,dst,150,255,0)
    display(dst,"Destination Image")
    cv.WaitKey(0)

if __name__=='__main__':
    thresholding()
