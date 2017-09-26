import cv2

#Diff images at times t0, t1, t2 to find change
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)
s, img = cam.read()

windowName = "Vroom, Vroom"
windowWebcam = "Boring Webcam"


#Read three images, convert to greyscale (limit color space)
tMinus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
tZero = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
tPlus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


print ("Tänk på hur du kör!")

while s:
    cv2.imshow(windowName, diffImg(tMinus, tZero, tPlus))

    # Read next image
    tMinus = tZero
    tZero = tPlus
    tPlus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


    ## Debug webcam window
    s, img = cam.read()
    cv2.imshow(windowWebcam, img)


    key = cv2.waitKey(10)
    if key == 27: ##ESCAPE 
        cv2.destroyWindow(windowName)
        break

print ("Sen var de bara nio!")
