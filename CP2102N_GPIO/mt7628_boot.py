import sys
import usb.core
# find USB devices
#dev = usb.core.find(find_all=True)
# loop through devices, printing vendor and product ids in decimal and hex
#for cfg in dev:
#    print(cfg)
#    print('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
#    print('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')


import time
import usb.core
import usb.util

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

#while True:

print("set CS1 to Hihg")
wIndex = 0xf9ff
dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
time.sleep(1)
print("set CS1 to High & RST mt7628")
wIndex = 0xfdff
dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
time.sleep(1)
print("set CS1 to High & release RST")
wIndex = 0xf9ff
dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
