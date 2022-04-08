import pyautogui
import time

x = 3
time.sleep(5)
pyautogui.write(str(x))
with pyautogui.hold('ctrl'):
    pyautogui.press('left', presses=1, interval=0.01)
x += 1
while x != 600:
    pyautogui.press('down', presses=6, interval=0.01)
    pyautogui.write(str(x))
    with pyautogui.hold('ctrl'):
        pyautogui.press('left', presses=1, interval=0.01)

    x += 1
