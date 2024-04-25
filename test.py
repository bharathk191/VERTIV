import pyautogui
import time
import keyboard
import sys

pyautogui.FAILSAFE = False
#looping while loop
while True:
    time.sleep(5)
    for i in range(0, 100):
        pyautogui.moveTo(0, i * 5)
        for i in range(0, 3):
            pyautogui.press('shift')
        if keyboard.is_pressed('Q'):
            sys.exit()