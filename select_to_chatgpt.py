#selected text
import os
from psutil import Process

#keyboard input
from pynput import keyboard

#chatgpt
from chatgpt_wrapper import ChatGPT

#multithreading
import threading
from gevent import monkey
monkey.patch_all()

#globals
bot = ChatGPT()
COMBINATION = {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.Key.space}
current = set()
threads = []
behavior = 'Write a program in python that '
"""
replace the above line with one of these if you want:

behavior = 'Write a program in python that '
behavior = 'Write a program in C that ' 
behavior = 'Write a story about '

"""

#processes the text and sends it to chatGPT
def process():
    message = os.popen('xsel').read()
    print(f"Your prompt was: \n\
            '{message}'\n\
            Generating output.")

    response = bot.ask(behavior + message)
    print(response)

#when combination is pressed logic
def on_all():
    print("Starting to process ChatGPT response...")
    thread = threading.Thread(target=process, daemon=True).start()

#on key press logic
def on_press(key):
    if key in COMBINATION:
        print(key)
        current.add(key)
        if all(k in current for k in COMBINATION):
            on_all()

#on key release logic
def on_release(key):
    if key in COMBINATION:
        current.discard(key)

#read keys
def main():
    with keyboard.Listener(
        on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        os._exit(1)
        
