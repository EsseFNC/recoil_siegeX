# F10 to start/stop the script
# ESC to quit

from pynput.mouse import Button
from pynput.mouse import Listener
from pynput import keyboard
import pyautogui

can_listen_mouse = True

def on_click(x, y, button, pressed):
    
    while True:
        if button == Button.left:
            pyautogui.move(0, 5, duration=.01)
        else:
            pressed = False
            
        if not pressed:
            break
        
    return False if can_listen_mouse else True
     
def on_press(key):
    global can_listen_mouse
    
    mouse_listener = Listener(on_click=on_click)
    
    if key == keyboard.Key.f10: # start/stop mouse listeners
        print("got F10")
        
        if can_listen_mouse:
            mouse_listener.start()
            # mouse_listener.join()
            can_listen_mouse = False
        else:
            can_listen_mouse = True
            
    if key == keyboard.Key.esc: # exit program code
        print("got ESC. Exiting program")
        exit(-1)
        
    

if __name__ == "__main__":
    # mouse_listener = Listener(on_click=on_click)
    # mouse_listener.start()
    
    # keyboard_listener = keyboard.Listener(on_press=on_press)
    # keyboard_listener.start()
    
    print('Press F10 to start/stop the script')
    print('Press ESC to quit')
    
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()
    
    
    
    