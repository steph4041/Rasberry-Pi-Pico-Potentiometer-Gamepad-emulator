# Rasberry-Pi-Pico-Potentiometer-Gamepad-emulator
the code is in circuitpython and it uses 4 buttons and 3 potentiometers to emulate a little joystick for assetto corsa (or any game that lets you modify the gamepad settings) 

The buttons are in GPIOs 16, 0, 1, 2 (they need to be connected to 3.3V on one side, and their GPIO pin on the other) 

Potentiometers are in GPIOs 26, 27, 28

NOTE: all variables names are in italian (I'm lazy)

To use this script, install circuitpython on your Rasberry pi pico and restart it. Then it should be as easy as drag and drop (assuming you connected everything correctly)

To verify if the script is working, just open any app that let you see the gamepads connected (even the windows game device configuration will be fine) and you should see a gamepad called "CircuitPython HID".

I know that the lib/adafruit_hid folder is very messy but I don't really want to organize it :)


WARNING
The variable called "frizione" (clutch in english) is translated into a joystick axis because that's what a lot of games use.
If you want the clutch to be another potentiometer buy a rasberry pi with more ADCs.
If the clutch isnt recognized, open the script and remove the # below "if frizione.value:"; this will move the clutch alongside the "sterzo" (steering in english)(only moves when the button is pressed) making it easier for the game to recognise; don't forget to put the # back tho!
