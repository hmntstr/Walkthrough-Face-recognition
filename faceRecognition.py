#from scipy import linalg
#import scipy as sp
from numpy import*
import cv2
import time
import numpy as np
po=[]
po1=[]
a=0

ret = True
cap = cv2.VideoCapture('output.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ((cv2.waitKey(1) & 0xFF == ord('q'))|ret==False):
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    po1.append(gray)
    a=a+1
    a1=cv2.resize(gray,None,fx=0.03125, fy=0.03125, interpolation = cv2.INTER_CUBIC)
    po.append(a1)
    
#po=np.array(po)
cap.release()
cv2.destroyAllWindows()



time.sleep(2)
m=[]
x=[]

normdist=[]

po=np.array(po)
po1=np.array(po1)
mean=po.mean(axis=0)#mean
for i in range(0,a):
    m.append(po[i]-mean)
m=np.array(m)
z=np.hstack(m)#concatenate horizontally
f=transpose(z)
g=np.dot(z,f)
la,v=linalg.eig(g)#Eigen's

for i in range(0,a):
    x.append(np.dot(v,m[i]))
x=np.array(x)
print "INSERT NEW IMAGE"
camera_port=0
ramp_frames=30
camera=cv2.VideoCapture(camera_port)
retval, im=camera.read()
k1 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
del(camera)
k=cv2.resize(k1,None,fx=0.03125, fy=0.03125, interpolation = cv2.INTER_CUBIC)

l=k-mean
m=np.dot(v,l)

for i in range(0,a):
    normdist.append(np.linalg.norm(x[i]-m))
normdist=np.array(normdist)
mini=min(normdist)
index=np.argmin(normdist)
print index
cv2.imshow("Face found", po1[index])
cv2.waitKey(0)
