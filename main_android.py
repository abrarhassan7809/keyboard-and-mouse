import time
from pynput.keyboard import Controller, Listener

# def controlmouse():
#     mouse = Controller()
#     mouse.position = (5, 200)
#
# controlmouse()

# time.sleep(3)
# def controlkeyboard():
#     keyboard = Controller()
#     keyboard.type('hello bro what are you doing')
#
# controlkeyboard()

# def on_press(key):
#     try:
#         print(f'alphanumeric key {key} pressed')
#     except AttributeError:
#         print(f'special key {key} pressed')
#
# def on_release(key):
#     print(f'{key} released')
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#
# # Collect events until released
# with keyboard.Listener(on_press=on_press, on_releas=on_release) as listener:
#     listener.join()
