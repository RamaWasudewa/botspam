import pyautogui
import time

message = "WEEEEEEE BANGUUUNNNNN !!!!!"
n = 50

time.sleep(3)

for i in range(n):
    pyautogui.typewrite(message + '\n')