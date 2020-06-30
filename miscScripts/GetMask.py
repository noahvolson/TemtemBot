import cv2
import numpy as np

def printArray(array):
    for row in array:
        print(row)

def imgToWalkable(img, val):
    imgArray = np.asarray(img)
    width = len(img[0])
    height = len(img)

    # trim image to 10px blocks
    width = (width // 10) * 10
    height = (height // 10) * 10

    # Array (list of lists) of tile statuses
    walkable = [[val for x in range(width//10)] for y in range(height//10)]   # One tile is 10 pixels


    for r in range(0, height, 10):
        for c in range(0, width, 10):
            for row in range(r, r+10):
                for col in range(c, c+10):
                    if ((imgArray[row][col] != (255,255,255,255)).any()):   # any tiles in chunk are non-white
                        walkable[row//10][col//10] = 0
                        break # if one pixel invalid, whole chunk invalid
                else:
                    continue
                break
            
    return walkable


frame = cv2.imread('Saipark.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

l_b1 = np.array([0, 0, 0])
u_b1 = np.array([97, 255, 159])

l_b2 = np.array([0, 0, 0])
u_b2 = np.array([88, 255, 200])

mask1 = cv2.inRange(hsv, l_b1, u_b1)# regular terrain
mask2 = cv2.inRange(hsv, l_b2, u_b2)# grass

cv2.imshow("mask1", mask1)
cv2.imshow("mask2", mask2)

array2 = imgToWalkable(mask2, 2)
