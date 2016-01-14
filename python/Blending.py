#blending two images
'''import cv2
from cv2 import cv
from GUI import  *
src=cv.LoadImage("C:\\Users\\raj\\Desktop\\image processing and computer vision\\pictures\\sa.jpg",cv.CV_LOAD_IMAGE_COLOR)
dst=cv.LoadImage("C:\\Users\\raj\\Desktop\\image processing and computer vision\\pictures\\s4.jpg",cv.CV_LOAD_IMAGE_COLOR)
def blending(alpha):
    cv.SetImageROI(src,(0,0,300,300))
    cv.SetImageROI(dst,(0,0,300,300))
    cv.AddWeighted(src,alpha,dst,1-alpha,0,dst)
    cv.ResetImageROI(src)
    cv.ResetImageROI(dst)
    cv.SaveImage("C:\\Users\\raj\\Desktop\\blended.jpg",dst)
    display(dst,"Destination")
    cv.WaitKey(0)
'''
import cv2
from cv2 import cv
#from GUI import display
src=cv.LoadImage("C:\\Users\\raj\\Desktop\\Python OpenCV\\sa.jpg",cv.CV_LOAD_IMAGE_COLOR)
dst=cv.LoadImage("C:\\Users\\raj\\Desktop\\Python OpenCV\\s4.jpg",cv.CV_LOAD_IMAGE_COLOR)
def blending(alpha):
    #src1=cv.GetSubRect(src,(0,0,300,300))
    #src2=cv.GetSubRect(dst,(0,0,300,300))
    cv.SetImageROI(src,(0,0,300,300))
    cv.SetImageROI(dst,(0,0,300,300))
    #display(src)
    #display(dst)
    cv.AddWeighted(src,alpha,dst,1-alpha,0,dst)
    #display(src)
    #display(dst)
    cv.ResetImageROI(src)
    cv.ResetImageROI(dst)
    cv.SaveImage("C:\\Users\\raj\\Desktop\\blended.jpg",dst)
    #display(src)
    cv.NamedWindow("Destination")
    cv.ShowImage("Destination",dst)
    cv.WaitKey(0)




#print cv.GetReal2D(src,0,0)[0] //GetReal*D support single channel images
#print cv.Get2D(src,0,0)

if __name__=='__main__':
    blending(0.5)
