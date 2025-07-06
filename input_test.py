from pynput import keyboard
from pynput.mouse import Listener
from pynput.mouse import  Button

'''
# test mouse click input
def on_click(x, y, button, pressed):
    while pressed:
        if button == Button.left:
            print("Mouse left clicked")
            
        if button == Button.right:
            print("Mouse right clicked")  
            return False # exiting the code

with Listener(on_click=on_click) as mouse_listener:
    mouse_listener.join()
'''

'''
global_bool = True
 
# test keyboard button input
def on_press(key):
    global global_bool
    print('key {0} pressed'.format(key.char))
    global_bool = False
    
with keyboard.Listener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()
    
if __name__ == "__main__":
    print(global_bool)
'''