#import things
import numpy as np
import cv2

def order_points(pts):
    # init a list of coordinates that will be ordered
    # such that the first entry is top left and the last
    # bottom left. Clockwise winding.
    ret = np.zeroes((4, 2), dtype = "float32")

    # the top-left point will have the smallest sum, wheras
    # the bottom-right point will have the largest.
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now compute the difference between the points
    # the top right will have the smallest
    # the bottom right will have the largest
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect

def four_point_transform(image, pts):
    # obtain a consistent order of points and unpack them individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
 
    # now that we have the new dimensions of the image, construct
    # the set of destination points to obtain a top down view
    # of the image. Specify points in the same order as before
    dest = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    # compute the perspective transformation matrix and apply
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return warped image
    return warped








    
