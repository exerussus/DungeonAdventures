import pyautogui
import time

# x = 600
# time.sleep(5)
# pyautogui.write(str(x))
# with pyautogui.hold('ctrl'):
#     pyautogui.press('left', presses=1, interval=0.01)
# x += 1
# while x != 656:
#     pyautogui.press('down', presses=6, interval=0.01)
#     pyautogui.write(str(x))
#     with pyautogui.hold('ctrl'):
#         pyautogui.press('left', presses=1, interval=0.01)
#
#     x += 1
x = 2
time.sleep(5)



x += 1


while x != 656:
    pyautogui.press('down', presses=6, interval=0.01)
    with pyautogui.hold('ctrl'):
        pyautogui.press('right', presses=5, interval=0.01)
    pyautogui.press(',', presses=1, interval=0.01)
    pyautogui.press('enter', presses=1, interval=0.01)
    pyautogui.write("'inspection': {")
    pyautogui.press('enter', presses=1, interval=0.01)

    x += 1