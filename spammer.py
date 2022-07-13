#!/usr/bin/python
import pyautogui
import webbrowser
import time


#ANSI
bold = "\033[1m"
light_green = "\033[1;32m"
yellow = "\033[1;33m"

banner = '''                      
	          333333     XX    XX          0000      888888
	            33       XX  XX      000000    00  88    88
	  rrrrrr    3333       XXXX      00        00    8888  
	  rr      33    33       XX      00        00  88    88
	  rr            33   XXXX  XX    00        00  88    88
	  rr       33333     XX      XX    00000000    888888  
             
                            SPAMMER\n                                                   '''
              
print(bold, banner)

speed = 1
message = input(" What message do you want to keep sending?  ")
repeats = int(input(" How many times do you want to send the message?  "))

print(yellow,"You have five seconds to refocus the text input area of your messaging app   ")
time.sleep(1)

isLoaded = input(" Press Enter when your messaging app is loaded up.  ")
time.sleep(5)


for i in range(0,repeats):         #Message loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press("enter")
		
		time.sleep(speed/100000)

print(light_green,"Done\n")
