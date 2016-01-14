#simple drawing
'''
import cv2
from cv2 import cv
from GUI import *
img=cv.LoadImageM("C:\\Users\\raj\\Desktop\\sa1.png",cv.CV_WINDOW_AUTOSIZE)
def ellipsedraw():
    cv.Ellipse(img,(50,150),(40,80),100.0,0.0,360.0,(0,0,0),8,2)
    display(img,"Destination")
    cv.WaitKey(0)

def linedraw():
    cv.Line(img,(0,0),(100,100),(0,0,0),4,8)
    display(img,"Destination")
    cv.WaitKey(0)

def drawrectangle():
    cv.Rectangle(img,(50,50),(100,100),(0,0,0),4,8)
    display(img,"Destination")
    cv.WaitKey(0)

def drawcircle():
    cv.Circle(img,(100,100),20,(0,0,0),4,8)
    display(img,"Destination")
    cv.WaitKey(0)
    
def drawfilledpolygon():
    cv.FillPoly(img,[[(50,50),(100,100)],[(120,20),(150,30)],[(50,50),(120,20)],[(100,100),(150,30)]],(255,255,255),4,1)
    display(img,"Destination")
    cv.WaitKey(0)


if __name__=='__main__':
    drawcircle()
    
'''

import cv2
from cv2 import cv
from GUI import *
from database import *
img=cv.LoadImageM(getpath(),cv.CV_WINDOW_AUTOSIZE)
def ellipsedraw():
    cv.Ellipse(img,(50,150),(40,80),100.0,0.0,360.0,(0,0,0),8,2)
    display(img,"Destination")
    cv.WaitKey(0)

def linedraw():
    cv.Line(img,(0,0),(100,100),(0,0,0),4,8)
    display(img,"Destination")
    cv.WaitKey(0)

def drawrectangle():
    cv.Rectangle(img,(50,50),(100,100),(0,0,0),4,8)
    display(img,"Destination")
    cv.WaitKey(0)

def drawcircle():
    cv.Circle(img,(100,100),20,(0,0,0),4,8)
    display(img,"Destination")
    cv.WaitKey(0)
    
def drawfilledpolygon():
    cv.FillPoly(img,[[(50,50),(100,100)],[(120,20),(150,30)],[(50,50),(120,20)],[(100,100),(150,30)]],(255,255,255),4,1)
    display(img,"Destination")
    cv.WaitKey(0)


if __name__=='__main__':
    drawcircle()
