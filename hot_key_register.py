# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:48:49 2020

@author: ACER
"""

import serial
import pyautogui
import os
import ctypes
    
    
try:
    arduino = serial.Serial("COM11",9600)
    print("CONNECTED!!")
    while 1:
        serialString = arduino.readline()
        x = int((serialString.decode("Ascii")))
        print(x)
        if x == 1:
            pyautogui.FAILSAFE = False
            pyautogui.press("f5")
            #pyautogui.hotkey("winleft", "m")
            #ctypes.windll.user32.LockWorkStation()
            x = 0

        if x == 2:
            pyautogui.FAILSAFE = False
            #pyautogui.press("f5")
            pyautogui.hotkey("winleft", "m")
            #ctypes.windll.user32.LockWorkStation()
            x = 0

        if x == 3:
            pyautogui.FAILSAFE = False
            #pyautogui.press("f5")
            pyautogui.hotkey("winleft", "m")
            ctypes.windll.user32.LockWorkStation()
            x = 0
            
            
except Exception as e:
    print("Not Found 404!!", e)
    