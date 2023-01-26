import socket
import os
from pynput import keyboard

COMBINATION = {keyboard.Key.ctrl, keyboard.Key.space}
current = set()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9999

def get():
    with keyboard.Listener(
        on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
	if key in COMBINATION:
		print(key)
		current.add(key)
		if all(k in current for k in COMBINATION):
			send()


def on_release(key):
    if key in COMBINATION:
        current.remove(key)


def send():
	print("here")
	clientsocket.send(os.popen('xsel').read().encode())


def main():
    # create a socket object


    def get_client():
        return clientsocket

    # connect to the server
    clientsocket.connect((host, port))

    get()
    # while message != "exit":
    #    clientsocket.send(message.encode())
    #    message = get_send(clientsocket)

    clientsocket.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
