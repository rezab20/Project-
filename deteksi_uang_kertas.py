import cv2
import numpy as np

def nothing(x):
 pass

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

image = cv2.imread('5RB.jpg')

while True :
    
    lh = cv2.getTrackbarPos('lowH', 'frame')
    hh = cv2.getTrackbarPos('highH', 'frame')
    ls = cv2.getTrackbarPos('lowS', 'frame')
    hs = cv2.getTrackbarPos('highS', 'frame')
    lv = cv2.getTrackbarPos('lowV', 'frame')
    hv = cv2.getTrackbarPos('highV', 'frame')

    #Membuat frame object
    #check, frame = video.read()
    ima = cv2.GaussianBlur(image, (9,9), 0)

    #Convert ke HSV
    hsv = cv2.cvtColor(ima, cv2.COLOR_BGR2HSV)

    #inRange warna
    # '''
    # lowerRED = np.array([10, 27, 222], np.uint8)
    # higherRED = np.array([13, 44, 255], np.uint8)
    # lowerYELLOW = np.array([13, 120, 0], np.uint8)
    # higherYELLOW = np.array([31, 255, 164], np.uint8)
    # '''
    lowerHSV = np.array([lh, ls, lv])
    higherHSV = np.array([hh, hs, hv])
    red = cv2.inRange(hsv, lowerHSV, higherHSV)
    #yellow = cv2.inRange(hsv, lowerYELLOW, higherYELLOW )

    #Morphological
    #res1 = cv2.bitwise_and(frame, hsv, mask = red)
    #res2 = cv2.bitwise_and(frame, hsv, mask = yellow)

    cv2.imshow("HSV", red)
    cv2.imshow("Asli", ima)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cv2.destroyAllWindows()