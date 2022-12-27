#created by AhmadRezaAnaami
import cv2
import numpy as np 


img = cv2.imread("1.jpg" , 1)
img = cv2.resize(img , [600,600])

def doSomething(index):
    pass


cv2.namedWindow('image')

cv2.createTrackbar('Kernel','image',1,145,doSomething)




while(1):

    
    if(cv2.getTrackbarPos('Kernel','image') % 2 == 0):
        r = cv2.getTrackbarPos('Kernel','image') + 1
    else:
        r = cv2.getTrackbarPos('Kernel','image')
    
    
    out = cv2.GaussianBlur(img,(r,r),sigmaX= 0  , sigmaY= 0  ) 
    cv2.imshow('image',out)
    k = cv2.waitKey(1) & 0xFF


cv2.destroyAllWindows()







