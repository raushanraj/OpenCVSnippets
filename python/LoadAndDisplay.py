#Load and Display an Image
'''from cv2 import cv
k="C:\\Users\\raj\\Desktop\\s4.jpg"
def LoadDisplay():
    img=cv.LoadImageM(k,cv.CV_LOAD_IMAGE_COLOR)
    print img
    cv.NamedWindow("LoadAndDisplay",cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage("LoadAndDisplay",img)
    cv.WaitKey(0)
    cv.DestroyWindow("LoadAndDisplay")

'''
from cv2 import cv
from database import *
k=getpath()
def LoadDisplay():
    img=cv.LoadImageM(k,cv.CV_LOAD_IMAGE_COLOR)
    print img
    cv.NamedWindow("LoadAndDisplay",cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage("LoadAndDisplay",img)
    cv.WaitKey(0)
    cv.DestroyWindow("LoadAndDisplay")

if __name__=='__main__':
    LoadDisplay()

    
    
    
