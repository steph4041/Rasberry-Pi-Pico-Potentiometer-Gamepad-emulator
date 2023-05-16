import analogio
import board
import time
import digitalio

bottone1 = digitalio.DigitalInOut(board.GP16)
bottone1.direction = digitalio.Direction.INPUT
bottone1.pull = digitalio.Pull.DOWN
frizione = digitalio.DigitalInOut(board.GP1)
frizione.direction = digitalio.Direction.INPUT
frizione.pull = digitalio.Pull.DOWN
marciagiu = digitalio.DigitalInOut(board.GP0)
marciagiu.direction = digitalio.Direction.INPUT
marciagiu.pull = digitalio.Pull.DOWN
marciasu = digitalio.DigitalInOut(board.GP2)
marciasu.direction = digitalio.Direction.INPUT
marciasu.pull = digitalio.Pull.DOWN


sterzo = analogio.AnalogIn(board.GP27)
freno = analogio.AnalogIn(board.GP26)
acceleratore = analogio.AnalogIn(board.GP28)
from hid_gamepad import Gamepad
import usb_hid
gamepad = Gamepad(usb_hid.devices)
while True:
    gamepad.move_joysticks(x=int(-(sterzo.value / 65535 * 254 - 127)), r_z=int(-(freno.value / 65535 * 254 - 127)), z=int(-(acceleratore.value / 65535 * 254 - 127)))
    time.sleep(0.001)
    
    #(acceleratore.value / 65535 * -127 + 127)
    #(((freno.value - 65535 )/ 65535 )* -127 - 127)
    #print("freno", (-(freno.value / 65535 * 254 - 127)))
    #print(acceleratore.value / 65535 * -127 + 127)
    #print(freno.value)
    if bottone1.value:
        gamepad.press_buttons(1)
    else:
        gamepad.release_buttons(1)
    if marciagiu.value:
        gamepad.press_buttons(2)
    else:
        gamepad.release_buttons(2)
    if marciasu.value:
        gamepad.press_buttons(3)
    else:
        gamepad.release_buttons(3)
    if frizione.value:
        #gamepad.move_joysticks(y=int(sterzo.value / 65535 * 254 - 127))
        gamepad.move_joysticks(y=127)
    else:
        gamepad.move_joysticks(y=-127)
    
        
    # if bottone2.value:
     #   gamepad.press_buttons(2)
    #else:
     #   gamepad.release_buttons(2)