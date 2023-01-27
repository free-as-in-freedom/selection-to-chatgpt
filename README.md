# selection-to-chatgpt
## Description
This is a program that when run, will take whatever text you have selected, and run chatgpt and return it to your terminal.

## Usage
Run the command `python3 select_to_chatgpt.py`, select some text, and hit the default key combination `control + alt + space`. This command can be changed.

## Dependencies
- [pynput](https://pypi.org/project/pynput/)
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) (Make sure to follow installation instructuins in the link)
- A ChatGPT enabled [OpenAI](https://chat.openai.com/) account
- [gevent](https://pypi.org/project/gevent/)

## Todo:
I'm currently working on making it work over TCP so that it can be used from a host machine to a remote server.
