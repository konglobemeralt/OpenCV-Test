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

    #return the ordered coordinates
    return rect

