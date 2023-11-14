from machine import Pin
from time import sleep

knop_zwart = Pin(17, Pin.IN)
knop_rood = Pin(16, Pin.IN)

PIN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
pin = []
for id in PIN: 
    pin.append(Pin(id, Pin.OUT))

for x in pin:
    x.off()
index =7

while True:
    sleep(0.2)
    print(index)
    if knop_zwart.value() == 1:
        pin[index].off()
        index +=1
        if index > 15:
            index= 15
    if knop_rood.value() == 1:
        pin[index].off()
        index -=1
        if index <0:
            index = 0
    pin[index].on()



    


 
