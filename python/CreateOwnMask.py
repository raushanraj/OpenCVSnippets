'''from cv2 import cv
import numpy
from GUI import *
ker=[[0,-1,0],[-1,5,-1],[0,-1,0]]
kernelnum=numpy.array(ker,dtype='f')
kernel=cv.fromarray(kernelnum,False)

def DoSimpleFilter():
    cv.Filter2D(src_image,dst_image,kernel,(-1,-1))
    display(dst_image,"Destination")
    cv.WaitKey(0)
'''
from cv2 import cv
import numpy
from GUI import *
ker=[[0,-1,0],[-1,5,-1],[0,-1,0]]
kernelnum=numpy.array(ker,dtype='f')
kernel=cv.fromarray(kernelnum,False)

def DoSimpleFilter():
    cv.Filter2D(src_image,dst_image,kernel,(-1,-1))
    display(dst_image,"Destination")
    cv.WaitKey(0)
if __name__=='__main__':
    DoSimpleFilter()


    
    
