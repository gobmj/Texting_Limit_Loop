# Code to loop a text, given the limit

import pyautogui as pt
import time
print("Welcome to the Loop Text Program\n")
limit = input("Enter Limit to Loop: ")
message = input("Enter message to Loop: ")
time.sleep(5)

i = 0

while i < int(limit):
    pt.typewrite(message)    
    pt.press("enter")
    i+=1
