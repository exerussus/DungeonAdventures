import pyautogui
import time

x = 33
time.sleep(5)
while x != 600:
    time.sleep(0.1)
    pyautogui.press('pagedown')
    time.sleep(0.1)
    pyautogui.press('pagedown')
    time.sleep(0.1)
    pyautogui.press('pagedown')
    time.sleep(0.1)
    pyautogui.press('pagedown')
    time.sleep(0.1)
    pyautogui.press('pagedown')
    time.sleep(0.1)
    pyautogui.press('pagedown')
    time.sleep(0.1)
    pyautogui.press('left')
    time.sleep(0.1)
    pyautogui.press('delete')
    time.sleep(0.1)
    pyautogui.write(str(x))
    time.sleep(0.1)
    x += 1