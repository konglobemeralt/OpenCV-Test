import cv2

cam = cv2.VideoCapture(0)
s, img = cam.read()

windowName = "Vroom, Vroom"
cv2.namedWindow('Front Camera')

while s:
    cv2.imshow(windowName, img)

    s, img = cam.read()

    if key == 27: ##ESCAPE 
        cv2.destroyWindow(winName)
        break

print ("Goodbye")
