import cv2
import numpy as np

def nothing(x):
 pass
"""
ilowH = 0
ihighH = 179
ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255
cv2.namedWindow('frame')
cv2.createTrackbar('lowH', 'frame', ilowH, 179, nothing)
cv2.createTrackbar('highH', 'frame', ihighH, 179, nothing)
cv2.createTrackbar('lowS', 'frame', ilowS, 255, nothing)
cv2.createTrackbar('highS', 'frame', ihighS, 255, nothing)
cv2.createTrackbar('lowV', 'frame', ilowV, 255, nothing)
cv2.createTrackbar('highV', 'frame', ihighV, 255, nothing)
""" 
#Upload video ke python
video = cv2.VideoCapture(0)

while True :
 """
 ilowH = cv2.getTrackbarPos('lowH', 'frame')
 ihighH = cv2.getTrackbarPos('highH', 'frame')
 ilowS = cv2.getTrackbarPos('lowS', 'frame')
 ihighS = cv2.getTrackbarPos('highS', 'frame')
 ilowV = cv2.getTrackbarPos('lowV', 'frame')
 ihighV = cv2.getTrackbarPos('highV', 'frame')
 """
 #Membuat frame object
 ret, frame = video.read()
 fra = cv2.GaussianBlur(frame,(5, 5), 0)

 #Convert ke HSV
 hsv = cv2.cvtColor(fra, cv2.COLOR_BGR2HSV)
 
 #inRange warna
 lowerRED = np.array([10, 27, 222], np.uint8)
 higherRED = np.array([13, 44, 255], np.uint8)
 lowerYELLOW = np.array([13, 120, 0], np.uint8)
 higherYELLOW = np.array([31, 255, 164], np.uint8)
 
 #lowerHSV = np.array([ilowH, ilowS, ilowV])
 #higherHSV = np.array([ihighH, ihighS, ihighV])
 red = cv2.inRange(hsv, lowerRED, higherRED)
 yellow = cv2.inRange(hsv, lowerYELLOW, higherYELLOW )

 #Morphological
 res1 = cv2.bitwise_and(frame, hsv, mask = red)
 res2 = cv2.bitwise_and(frame, hsv, mask = yellow)
 
 #Bounding box
 #100RB
 contours, hierarki = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   
 if(len(contours)>0):
  for contour in contours:
   area = cv2.contourArea(contour)
   if(area > 100):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(frame, '100.000', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
 
 #50RB
 contours,hierarki = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 if(len(contours)>0):
  for contour in contours:
   area = cv2.contourArea(contour)
   if(area > 500):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    cv2.putText(frame, '50.000', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255))
    
 cv2.imshow('image frame', frame)
 #Menampilkan frame
 cv2.imshow('hsv', hsv)
 cv2.imshow('Red', res1)
 cv2.imshow('Yellow', res2)
 key=cv2.waitKey(5)
 
 if key == ord('e'):
  break
 
#Menutup kamera
video.release()
cv2.destroyAllWindows()