import pyautogui
import time

print("Fishing Script")
print("Sleeping 5 seconds to tab in")
time.sleep(5)
(xp, yp) = pyautogui.position()
print("OK Clicking")
#while True:
pyautogui.mouseDown(button="right")
#time.sleep(0.25)

