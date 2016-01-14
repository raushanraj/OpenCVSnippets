"""
1. normalization for trainng set
2. In constructor pass the src image path and dst path without extension
3. return the dst image which is normalized and in jpg format(256X256)
"""


import os
import numpy as np
import cv2
from cv2 import cv

class normalize:
    def __init__(self,src,dst):
        self.src=src
        self.dst=dst+"_1.jpg"
    def resize(self):
        x,y=256,256
        src=cv2.imread(self.src,1)
        src=cv2.resize(src,(x,y))
        cv2.imwrite(self.dst,src)
        dst=cv2.imread(self.dst,1)
        return dst

def segmentation(src):
    img=src.copy()
    img=cv2.cvtColor(src,cv.CV_BGR2YCrCb)
    dst=cv2.inRange(img,(0,133,77),(255,173,127))
    return dst

class imagezone:
	def __init__(self,src):
		self.src=src
		self.zone1=src.copy()
		self.zone2=src[30:226,30:226]
		self.zone3=src[60:196,60:196]
	def getzone1(self):
		self.zone1=src[60:196,60:196]
		return self.zone1
	
		
		
	   
src=normalize("1.jpg","1").resize()
dst=segmentation(src)
cv2.imshow("org",dst)
cv2.imshow("new",src)
"""zone1=src[50:206,50:206]
zone2=src[80:176,80:176]
cv2.rectangle(zone1,(30,30),(116,116),(0,0,0),-1)
#zone1[30:116,30:116]=[0,0,0]"""
zone1=src[30:226,30:226]
zone2=src[60:196,60:196]
zone3=src[90:166,90:166]
cv2.imshow("a",zone1)
cv2.imshow("b",zone2)
cv2.imshow("c",zone3)
  
cv2.waitKey(0)


"""img=normalize("source.jpg","source").resize()
cv2.imshow("check",img)
cv2.waitKey(0)"""
    
