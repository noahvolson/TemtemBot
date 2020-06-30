import cv2
import numpy as np
import pyautogui
import time
from PIL import Image, ImageDraw
from Astar import *

def sumArrays(arr1, arr2, dest):
    for i in range(len(arr1)):    
        for j in range(len(arr1[0])): 
            dest[i][j] = arr1[i][j] + arr2[i][j]

def imgToWalkable(img, tolerance):
    imgArray = np.asarray(img)
    width = len(img[0])
    height = len(img)

    # trim image to 10px blocks
    width = (width // 10) * 10
    height = (height // 10) * 10

    # Array (list of lists) of tile statuses
    walkable = [[1 for x in range(width//10)] for y in range(height//10)]   # One tile is 10 pixels


    for r in range(0, height, 10):
        for c in range(0, width, 10):
            blackPix = 0 # number of black pixels in a chunk
            for row in range(r, r+10):
                for col in range(c, c+10):
                    if ((imgArray[row][col] != (255,255,255,255)).any()):   # pixels in chunk are non-white
                        blackPix = blackPix + 1

                    if (blackPix > tolerance):
                        walkable[row//10][col//10] = 0
                        break # if exceed tolerance, whole chunk invalid
                else:
                    continue
                break
            
    return walkable

def tupleToKey(r,c):
    return {
        (1,0): ('w', ''),
        (1,1): ('w','a'),
        (0,1): ('a',''),
        (-1,1): ('a','s'),
        (-1,0): ('s',''),
        (-1,-1): ('s','d'),
        (0,-1): ('d',''),
        (1,-1): ('d','w'),
        
        # Mirrored presses for walk back
        ('w', ''): ('s',''),
        ('w','a'): ('s','d'),
        ('a',''): ('d',''),
        ('a','s'): ('d','w'),
        ('s',''): ('w', ''),
        ('s','d'): ('w','a'),
        ('d',''): ('a',''),
        ('d','w'): ('a','s'),
        
    }[r,c]

def pathToKeyPresses(path):
    keyPresses = []
    for i in range(len(path) - 1):
        keyPresses.append(tupleToKey(path[i][0] - path[i+1][0], path[i][1] - path[i+1][1]))

    # add the reverse path for full loop
    for keyPress in keyPresses[len(keyPresses):None:-1]:
        keyPresses.append(tupleToKey(keyPress[0],keyPress[1]))

    return keyPresses


def initWalkable():
    frame = cv2.imread("Saipark.png")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b1 = np.array([0, 0, 0])
    u_b1 = np.array([100, 255, 210])

    l_b2 = np.array([0, 0, 0])
    u_b2 = np.array([88, 255, 200])

    l_b3 = np.array([0, 172, 144])
    u_b3 = np.array([255, 255, 255])

    mask1 = cv2.inRange(hsv, l_b1, u_b1)# all terrain
    mask2 = cv2.inRange(hsv, l_b2, u_b2)# grass
    mask3 = cv2.inRange(hsv, l_b3, u_b3)# water

    # NOTE: Maybe just add a mask for Tucma waters?
    #cv2.imshow("mask1", mask1)
    #cv2.imshow("mask2", mask2)
    #cv2.imshow("mask3", mask3)

    terrain = imgToWalkable(mask1,0)
    grass = imgToWalkable(mask2,40)
    water = imgToWalkable(mask3,40)

    width = len(terrain[0])
    height = len(terrain)
    weightedMap = [[0 for x in range(width)] for y in range(height)]

    # add all three arrays together
    sumArrays(terrain, grass, weightedMap)
    sumArrays(water, weightedMap, weightedMap)

    return weightedMap
