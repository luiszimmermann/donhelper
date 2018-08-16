import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

MOUSE_SPEED = 0.2
CHASE_MOB = 'chasemob.png'
MAXIMIZE = 'maximize.png'

def main():
    logging.info('Don Helper Started. Press Ctrl-C to abort at any time.')
    maximizeWindow()

def imPath(filename):
    return os.path.join('images', filename)

def moveToAndClick(x, y):
    pyautogui.moveTo(x, y, MOUSE_SPEED)
    pyautogui.click()

def maximizeWindow():
    x, y = pyautogui.locateCenterOnScreen(imPath(MAXIMIZE), grayscale=False)
    moveToAndClick(x, y)

def checkChase():
    x, y = pyautogui.locateCenterOnScreen(imPath(CHASE_MOB), grayscale=False)
    moveToAndClick(x, y)

if __name__ == '__main__':
    main()