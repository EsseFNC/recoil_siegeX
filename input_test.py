import pynput
from pynput.mouse import Listener
from pynput.mouse import  Button

def on_click(x, y, button, pressed):
    if button == Button.left:
        print("Mouse clicked")   

with Listener(on_click=on_click) as listener:
    listener.join()