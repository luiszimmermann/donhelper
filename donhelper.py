#! python3
"""Don Helper
"""

import pyautogui, threading, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

MOUSE_SPEED = 0.2
CHASE_MOB = 'chasemob.png'
MAXIMIZE = 'maximize.png'

def main():
    logging.info('Don Helper Started. Press Ctrl-C to abort at any time.')
    maximizeWindow()
    startHelping()

def imPath(filename):
    return os.path.join('images', filename)

def moveToAndClick(pos):
    pyautogui.moveTo(pos, duration = MOUSE_SPEED)
    pyautogui.click()

def locateImageAndClick(image):
    pos = pyautogui.locateCenterOnScreen(imPath(image), grayscale=False)
    if pos is not None:
        moveToAndClick(pos)

def maximizeWindow():
   locateImageAndClick(MAXIMIZE)

def checkChase():
    locateImageAndClick(CHASE_MOB)

def prepareGame():
    checkChase()

def stopHelping():
    '''Se o mouse chegar no 0x ou no 0y, o programa para'''
    while True:
        time.sleep(0.2)
        x, y = pyautogui.position()
        if x == 0 or y == 0:
            logging.info('Don Helper Closed.')
            os._exit(1)

def startHelping():
    st = threading.Thread(target=stopHelping)
    st.start()

if __name__ == '__main__':
    main()