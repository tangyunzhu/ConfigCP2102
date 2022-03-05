import time
import usb.core
import usb.util

#---------------------wIndex bit format------------------------#
#bit 7      6       5       4       3       2       1       0
#    1      1       1       1       GPIO.3  GPIO.2  GPIO.1  GPIO.0


#

PID = 0xea60
VID = 0x10c4

dev = usb.core.find(idVendor=VID, idProduct=PID)
if not dev:
        print("CP2104 was not found!")
        exit(1)
print("Yeeha! Found CP2104")

reqType = 0x41
bReq = 0xFF
wVal = 0x37E1

while True:

        wIndex = 0xffff
        print("toggling On")
        dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
        time.sleep(1)
        print("toggling Off")
        wIndex = 0x00ff
        dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
        time.sleep(1)
