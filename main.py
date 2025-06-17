from pynput.mouse import Button
from pynput.mouse import Listener
from pynput import keyboard
import pyautogui

def on_click(x, y, button, pressed):
    if button == Button.left:
        pyautogui.moveTo(x=None, y=466)
        pyautogui.moveTo(x=None, y=500, duration=2)
        # pyautogui.dragTo(x=802, y=500, duration=5)
        # print(pyautogui.position()) # DEBUG
        
def on_press(key):
    if key.char == 'a':
        pass # TODO: find a way to pass can_listen_mouse to this function

if __name__ == "__main__":
    mouse_listener = Listener(on_click=on_click)
    mouse_listener.start()
    
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    
    can_listen_mouse = False
    print('Press Ctrl-C to quit')
    
    try:
        while True:
            if can_listen_mouse:
                mouse_listener.wait()
    except KeyboardInterrupt:
        print('\n')
    