#video capture from webcam
'''import cv2
from cv2 import cv


def capturevideo():
    cv.NamedWindow("RED BALL DETECTION",cv.CV_WINDOW_AUTOSIZE)
    cv.NamedWindow("ORIGINAL IMAGE",cv.CV_WINDOW_AUTOSIZE)
    capture=cv.CaptureFromCAM(0)
    frame=cv.QueryFrame(capture)
    dst_image=cv.CreateImage((frame.width,frame.height),8,1)
    cv.ShowImage("RED BALL DETECTION",frame)
    if capture:
        while True:
            frame=cv.QueryFrame(capture)
            if not frame:
                break
            cv.ShowImage("ORIGINAL IMAGE",frame)
            cv.InRangeS(frame,cv.Scalar(0, 0, 200),cv.Scalar(140, 110, 255),dst_image)
            cv.ShowImage("RED BALL DETECTION",dst_image)
            cv.ShowImage("ORIGINAL IMAGE",frame)
            key=cv.WaitKey(33)
            if key==27:
                break
    cv.DestroyWindow("RED BALL DETECTION")
    cv.DestroyWindow("ORIGINAL IMAGE")'''
import cv2
from cv2 import cv


def capturevideo():
    cv.NamedWindow("RED BALL DETECTION",cv.CV_WINDOW_AUTOSIZE)
    cv.NamedWindow("ORIGINAL IMAGE",cv.CV_WINDOW_AUTOSIZE)
    capture=cv.CaptureFromCAM(0)
    frame=cv.QueryFrame(capture)
    dst_image=cv.CreateImage((frame.width,frame.height),8,1)
    cv.ShowImage("RED BALL DETECTION",frame)
    if capture:
        while True:
            frame=cv.QueryFrame(capture)
            if not frame:
                break
            cv.ShowImage("ORIGINAL IMAGE",frame)
            cv.InRangeS(frame,cv.Scalar(0, 0, 200),cv.Scalar(140, 110, 255),dst_image)
            cv.ShowImage("RED BALL DETECTION",dst_image)
            cv.ShowImage("ORIGINAL IMAGE",frame)
            key=cv.WaitKey(33)
            if key==27:
                break
    cv.DestroyWindow("RED BALL DETECTION")
    cv.DestroyWindow("ORIGINAL IMAGE")
if __name__=='__main__':
    capturevideo()
