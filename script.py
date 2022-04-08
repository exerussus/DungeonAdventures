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


while x != 656:
    pyautogui.press('down', presses=6, interval=0.01)
    with pyautogui.hold('ctrl'):
        pyautogui.press('right', presses=5, interval=0.01)
    pyautogui.press(',', presses=1, interval=0.01)
    pyautogui.press('enter', presses=1, interval=0.01)
    pyautogui.press("'")
    pyautogui.press('i')
    pyautogui.press('n')
    pyautogui.press('s')
    pyautogui.press('p')
    pyautogui.press('e')
    pyautogui.press('c')
    pyautogui.press('t')
    pyautogui.press('i')
    pyautogui.press('o')
    pyautogui.press('n')
    pyautogui.press('right', presses=1, interval=0.01)
    pyautogui.press(":")
    pyautogui.press("space")
    pyautogui.press("{")
    pyautogui.press('enter', presses=1, interval=0.01)

    pyautogui.press("'")
    pyautogui.press("t")
    pyautogui.press("r")
    pyautogui.press("u")
    pyautogui.press("e")
    pyautogui.press('right', presses=1, interval=0.01)
    pyautogui.press(":")
    pyautogui.press("space")
    pyautogui.press("'")
    pyautogui.press('right', presses=1, interval=0.01)
    pyautogui.press(',', presses=1, interval=0.01)
    pyautogui.press('enter', presses=1, interval=0.01)

    pyautogui.press("'")
    pyautogui.press("f")
    pyautogui.press("a")
    pyautogui.press("l")
    pyautogui.press("s")
    pyautogui.press("e")
    pyautogui.press('right', presses=1, interval=0.01)
    pyautogui.press(":")
    pyautogui.press("space")
    pyautogui.press("'")
    pyautogui.press('right', presses=1, interval=0.01)
    pyautogui.press(',', presses=1, interval=0.01)
    pyautogui.press('enter', presses=1, interval=0.01)
    pyautogui.press('down', presses=1, interval=0.01)
    x += 1