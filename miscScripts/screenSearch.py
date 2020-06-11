import pyautogui
import cv2


# determine whether we have found an IMG onscreen
def foundIMG(fileName):
    try:
        x,y = pyautogui.locateCenterOnScreen(fileName, confidence=0.9)
        print("FOUND IMG")
        return True
    except:
        print("NOT FOUND")
        return False

print("Please enter the name of your image with file extension:")
fileName = input()

print(foundIMG(fileName))
