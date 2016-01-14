'''from cv2 import cv
from GUI import *
def convert():
    im=cv.LoadImageM("C:\\Users\\raj\\Desktop\\s4.jpg")
    cv.SaveImage("C:\\Users\\raj\\Desktop\\s5.png",im)
    display(im,"PNG FROM JPG")
    cv.WaitKey(0)
    '''


from cv2 import cv
from GUI import *
def convert():
    im=cv.LoadImageM(getpath())
    cv.SaveImage("C:\\Users\\raj\\Desktop\\s5.png",im)
    display(im,"PNG FROM JPG")
    cv.WaitKey(0)
    
if __name__=='__main__':
    convert()
