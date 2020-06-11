from numpy import random
import pyautogui
import cv2
import time

# determine whether battle sequence has started 
def notInBattle():
    if pyautogui.pixelMatchesColor(1765, 154, (52, 21, 34)):
        print("PEACE")
        return True
    else:
        print("BATTLE SEQUENCE STARTED")
        return False

# determine whether battle sequence has finished loading
def sequenceFinished():
    if pyautogui.pixelMatchesColor(970, 1007, (34, 253, 255)):
        print("BATTLE SEQUENCE FINISHED")
        return True
    else:
        print("LOADING")
        return False

# determine whether we have found a luma
def foundLuma():
    try:
        x,y = pyautogui.locateCenterOnScreen('LumaIcon.png', confidence=0.9)
        print("FOUND LUMA")
        return True
    except:
        print("NOT LUMA")
        return False

# log out of account
# def logout():

# track which keys are pressed down so they are released naturally (start by moving forward)
keyStatus = {
  'w': 1, 
  'a': 0,
  's': 0,
  'd': 0
}

tileRGB = {
  1: (112, 171, 132),   # grass
  2: (0, 127, 178),     # water
  3: (52, 121, 132),    # underground
  4: (195, 82, 110),    # toxic water
  5: (19, 125, 165)     # Tucma/Omninesia water
}

start = time.time()
current = start

print ("what tileset are you searching?\n1 - grass\n2 - Deniz water\n3 - underground\n4 - toxic water\n5 - Tucma/Omninesia water")
RGB = tileRGB[int(input())]


print("press [Enter] to start")
begin = input()

time.sleep(3)

while (current - start) < 1000: # while uptime < 60 seconds TODO: CHANGE THIS

    # ------------------------ SEARCHING ------------------------

    pyautogui.keyDown('w')
    while notInBattle(): # note: 2x ESC at random places to generate fake pivot points?
        if not (pyautogui.pixelMatchesColor(1764, 144, RGB)):# hit top
            print("HIT TOP")
            pyautogui.keyUp('w')
            time.sleep(abs(random.normal(loc=.05, scale=.01)))
            pyautogui.keyDown('s')
        elif not (pyautogui.pixelMatchesColor(1765, 165, RGB)):# hit bottom
            print("HIT BOTTOM")
            pyautogui.keyUp('s')
            time.sleep(abs(random.normal(loc=.05, scale=.01)))
            pyautogui.keyDown('w')

    # ---------------------- FOUND TEMTEM ------------------------
    
    # release all keys
    for x in keyStatus:
        pyautogui.keyUp(x)
        keyStatus[x] = 0

    while not sequenceFinished():
        continue

    time.sleep(abs(random.normal(loc=.2, scale=.05)))

    if foundLuma():
        break
    else:
        # not a luma, flee and continue
        pyautogui.press('8')
        time.sleep(abs(random.normal(loc=.1, scale=.05)))
        pyautogui.press('8')
        time.sleep(5)
    current = time.time()
# logout
