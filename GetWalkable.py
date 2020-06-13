from PIL import Image
from numpy import asarray

def printArray(array):
    for row in array:
        print(row)
 
img = Image.open("BlackSquares.png")
width, height = img.size
imgArray = asarray(img)

# trim image to 10px blocks
width = (width // 10) * 10
height = (height // 10) * 10

# Array (list of lists) of tile statuses
walkable = [[1 for x in range(width//10)] for y in range(height//10)]   # One tile is 10 pixels


for r in range(0, height, 10):
    for c in range(0, width, 10):
        for row in range(r, r+10):
            for col in range(c, c+10):
                if ((imgArray[row][col] != (255,255,255,255)).any()):   # any tiles in chunk are non-white
                    walkable[row//10][col//10] = 0
                    break
            else:
                continue
            break

printArray(walkable)
