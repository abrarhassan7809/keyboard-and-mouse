import time
import pyautogui
from pynput.mouse import Controller, Listener

def auto_mouse_move():
    pyautogui.click(20, 300, duration=1)
    pyautogui.click(550, 48, duration=1)
    time.sleep(1)
    pyautogui.typewrite("open youtube")
    pyautogui.hotkey('enter')
    pyautogui.click(362, 329, duration=1)
    time.sleep(1)
    pyautogui.hotkey('enter')

auto_mouse_move()

# --------------------

# def write_file(x, y):
#     print(f"The current position is {(x, y)}")
#
# with Listener(on_move=write_file) as l:
#     l.join()
