import cv2

cam = cv2.VideoCapture(0)
s, img = cam.read()

windowName = "Vroom, Vroom"
cv2.namedWindow('Front Camera')

print ("Tänk på hur du kör!")

while s:
    cv2.imshow(windowName, img)
    s, img = cam.read()

    key = cv2.waitKey(10)
    if key == 27: ##ESCAPE 
        cv2.destroyWindow(windowName)
        break


