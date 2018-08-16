import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

CHASE_MOB = 'chasemob.png'

def main():
    logging.info('Don Helper Started. Press Ctrl-C to abort at any time.')
    checkChase()

def imPath(filename):
    return os.path.join('images', filename)

def checkChase():
    x, y = pyautogui.locateCenterOnScreen(imPath(CHASE_MOB), grayscale=False)
    pyautogui.click(x, y)

if __name__ == '__main__':
    main()