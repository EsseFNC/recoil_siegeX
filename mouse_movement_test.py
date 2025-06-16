import pyautogui
from pyautogui import Point

pyautogui.moveTo(x=802, y=466)
# pyautogui.drag(xOffset=802, yOffset=500, duration=5)
pyautogui.dragTo(x=802, y=500, duration=5)
# print(pyautogui.position())