import cv2
import numpy as np
import matplotlib.pyplot as plt# import pyplot as plt
font = cv2.FONT_HERSHEY_COMPLEX

#ambil dan resize
ori = cv2.imread('baru/kirim/3i.jpg',1)
img = cv2.resize(ori, (550,450))

#Daun Bawang
#Filter,ColorSpace,Segmentasi
blurB = cv2.GaussianBlur(img,(5,5),0)
hsvB = cv2.cvtColor(blurB, cv2.COLOR_BGR2HSV)#88,28,43
lowerBlue = np.array([90,0,0], dtype=np.uint8)
upperBlue = np.array([100,255,255], dtype=np.uint8)

maskingB = cv2.inRange(hsvB,lowerBlue, upperBlue)
hasilB = cv2.bitwise_and(img,img, mask = maskingB)
ret,canyB = cv2.threshold(maskingB,96,120,cv2.THRESH_BINARY)
blurB2 = cv2.medianBlur(canyB , 3)
#morphology
kerneldB = np.ones((8,7), np.uint8)
kerneleB = np.ones((3,2), np.uint8)

dilationB = cv2.dilate(blurB2, kerneldB, iterations=7)
erotionB = cv2.erode(dilationB, kerneleB, iterations=2)

#find contours
contours, hierarchy= cv2.findContours(erotionB, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
#hierarchy = cv2.findContours(erotionB, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
final = cv2.bitwise_and(img, img, mask=erotionB)
#img_contours = np.zeros(img.shape)
for c in contours:
    area = cv2.contourArea(c)
    peri1 = cv2.arcLength(c, True)
    approx1 = cv2.approxPolyDP(c, 0.0001 * peri1, True)#cv2.drawContours(img, contours, -1, (0,255,0), 3)
    if cv2.contourArea(c) > 10000:#1000 <  area < 7000:
        #cv2.drawContours(img_contours1, [approx1], -1, (0, 0, 255), 1)
        #perimeter = perimeter + peri
        x,y,w,h = cv2.boundingRect(c) 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.putText(img, "Daun Bawang", (x, y),font,(0.7), (0,0,255))
#print(area)
cv2.imshow('r11.jpg', img)
cv2.imwrite('hasil/3i(90-100).jpg',hasilB)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()