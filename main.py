from pynput.mouse import Button
from pynput.mouse import Listener
import pyautogui

def on_click(x, y, button, pressed):
    if button == Button.left:
        pyautogui.moveTo(x=802, y=466)
        pyautogui.moveTo(x=802, y=500, duration=5)
        # pyautogui.dragTo(x=802, y=500, duration=5)
        # print(pyautogui.position()) # DEBUG

if __name__ == "__main__":
    listener = Listener(on_click=on_click)
    listener.start()
    while True:
        listener.wait()
    