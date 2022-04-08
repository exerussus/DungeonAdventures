import pyautogui
import time

x = 33
time.sleep(5)
while x != 600:
    pyautogui.press('down', presses=6, interval=0.05)
    pyautogui.press('left', presses=1, interval=0.05)
    pyautogui.press('backspace', presses=1, interval=0.05)
    pyautogui.write(str(x))
    x += 1
