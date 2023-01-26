import socket
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()

def process_message(message):
    print(f"Recieved '{message}' from user")
    # your message processing logic here
    response = bot.ask(message)
    print(response)  # prints the response from chatGPT
    pass

def main():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = 'localhost'

    port = 9999

    # bind to the port
    serversocket.bind((host, port))

    # queue up to 5 requests
    serversocket.listen(5)

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))

        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            process_message(data)

    clientsocket.close()

if __name__ == '__main__':
    main()
