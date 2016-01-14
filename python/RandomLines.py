#random line generator
'''from cv2 import cv
from random import Random
def drawrandline():
    rand=Random()
    img=cv.CreateImage((700,1000),8,3)
    cv.SetZero(img)
    cv.NamedWindow("RandomViewer",1)
    for i in range(100):
        cv.Line(img,(rand.randrange(0,700),rand.randrange(0,1000)),(300,200),(rand.randrange(0,256),rand.randrange(0,256),rand.randrange(0,256)),1,8,0)
        cv.ShowImage("RandomViewer",img)
        cv.WaitKey(5)
    cv.PutText(img,"Hello OpenCV",(100,200),cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,5,10,0,1,8),(255,255,255))
    cv.ShowImage("RandomViewer",img)
    cv.WaitKey(5)'''
from cv2 import cv
from random import Random
def drawrandline():
    rand=Random()
    img=cv.CreateImage((700,1000),8,3)
    cv.SetZero(img)
    cv.NamedWindow("RandomViewer",1)
    for i in range(100):
        cv.Line(img,(rand.randrange(0,700),rand.randrange(0,1000)),(300,200),(rand.randrange(0,256),rand.randrange(0,256),rand.randrange(0,256)),1,8,0)
        cv.ShowImage("RandomViewer",img)
        cv.WaitKey(5)
    cv.PutText(img,"Hello OpenCV",(100,200),cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,5,10,0,1,8),(255,255,255))
    cv.ShowImage("RandomViewer",img)
    cv.WaitKey(0)
    cv.DestroyWindow("RandomViewer")


if __name__=='__main__':
    drawrandline()
    
    
    
    
    
