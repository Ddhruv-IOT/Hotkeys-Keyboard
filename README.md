# Hotkeys Keyboard

<br/>

![Blue Illustrated Technology General LinkedIn Banner (1)](https://github.com/Ddhruv-IOT/Hot-Keyboard-Automation/assets/54676859/41488a16-005e-4d21-9ecd-a940db4dfd30)

<br/>

## About Project 😎😎

Introducing the **Hotkeys Keyboard**, a revolutionary tool designed to revolutionize your productivity. With its sleek design and intuitive functionality, this innovative device is a game-changer for anyone seeking to streamline their workflow. Featuring three strategically placed buttons, the Hotkeys Keyboard enables quick and effortless execution of essential tasks. Whether it's running Python code with a single press, minimizing all windows to declutter your screen, or locking your workstation for enhanced security, this compact and efficient solution is here to elevate your efficiency. Say goodbye to time-consuming shortcuts and welcome a new era of speed and productivity with the Hotkeys Keyboard.

## Tools and Technologies Used:

### Python Modules:
- PySerail, for Serial Communication
- PyAutoGUI, to simulate key press
  
### Softwares Used
- Anaconda
- Spyder IDE
- Arduino IDE
- Git Bash

### OS Used:
- Windows 10 

## Features
- Compact Keyboard
- Lightweight design
- Press the 1st button to execute Python Scripts
- Press the 2nd button to hide all Windows
- Press the 3rd button to lock the workstation

## Working

The Hotkeys Keyboard operates through a seamless combination of **hardware and software** components. The hardware setup includes an Arduino board and three push buttons connected to it. When a button is pressed, it sends a corresponding signal to the Arduino. The Arduino acts as a bridge between the buttons and the computer. On the software side, a Python script runs on the computer, waiting for input from the Arduino via serial communication. Once the Arduino receives a button press signal, it sends the corresponding signal to the Python script. The Python script interprets the signal and performs the associated action.

For example, when Button 1 is pressed, the Arduino sends a signal of "1" to the Python script. The Python script recognizes this signal as a request to execute the F5 key, which is commonly used to run Python code in Spyder. It emulates the F5 key press event, effectively running the code.

Similarly, when Button 2 is pressed, the Arduino sends a signal of "2" to the Python script. The Python script interprets this signal as a command to trigger the "Win+M" key combination, minimizing all open windows on the computer screen.

Lastly, when Button 3 is pressed, the Arduino sends a signal of "3" to the Python script. The Python script recognizes this signal as a request to lock the workstation, ensuring privacy and security.

***Through this seamless integration of hardware and software, the Hotkeys Keyboard provides users with a convenient and efficient way to execute essential functions with just a press of a button.***

# Thank you
- All suggestions are warmly welcomed.
