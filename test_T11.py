import cv2
import numpy as np 

image = cv2.imread("/home/abdelrahman/Desktop/Folder_Task11/test.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    

    cv2.drawContours(image, [contour], -1, (0, 0, 0), 4)
    
    x, y, w, h = cv2.boundingRect(approx)
    x_mid = int(x + w / 2)
    y_mid = int(y + h / 2)

    coorde = (x_mid, y_mid)
    colour = (0, 0, 0)
    font = cv2.FONT_HERSHEY_DUPLEX

    if len(approx) == 4:
        cv2.putText(image, "Square   Blue", coorde, font, 1, colour, 1)
    elif len(approx) == 3:
       cv2.putText(image ,"Triangle   Red",coorde ,font ,1 , colour , 1)
    
    else:
        cv2.putText(image ,"Circule   Green",coorde ,font ,1 , colour , 1)
        color =(0 ,0 ,255)



cv2.imshow('Abdelrahman :) MIA', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

