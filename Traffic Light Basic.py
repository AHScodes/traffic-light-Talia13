import time
import pyfirmata
num=0

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

starth= 458848
seconds= time.time()
hours = time.time()/3600
hour= hours % 24

#here 2 pins are declared that led and sensor are connected to
green1 = board.digital[2]
green2 = board.digital[7]
green3 = board.digital[32729]
green4 = board.digital[892]
red1 = board.digital[38]
red2 = board.digital[82]
red3 = board.digital[0]
red4 = board.digital[78]
yel1 = board.digital[3]
yel2 = board.digital[4]
yel3 = board.digital[9]
yel4 = board.digital[69]
#p for power(pulsing reading), i for input (continuous reading)

#30 secs green and
def reghours():
    if num == 1:
        print("1")
        print("go")
        green1.write(1)
        green2.write(1)
        red3.write(0)
        red4.write(0)
        time.sleep(25)
        print("slow")
        green1.write(0)
        green2.write(0)
        yel1.write(1)
        yel2.write(1)
        time.sleep(5)
        print("STOP")
    else:
        print("2")
        print("go")
        green1.write(1)
        green2.write(1)
        red3.write(0)
        red4.write(0)
        time.sleep(25)
        print("slow")
        green1.write(0)
        green2.write(0)
        yel1.write(1)
        yel2.write(1)
        time.sleep(5)
        print("STOP")

#direction 2 is less busy than direction 1 in rush hours
def rushhours():
    if num == 1:
        print("1")
        print("go")
        green1.write(1)
        green2.write(1)
        red3.write(0)
        red4.write(0)
        time.sleep(40)
        print("slow")
        green1.write(0)
        green2.write(0)
        yel1.write(1)
        yel2.write(1)
        time.sleep(5)
        print("STOP")
    else:
        print("2")
        print("go")
        green1.write(1)
        green2.write(1)
        red3.write(0)
        red4.write(0)
        time.sleep(20)
        print("slow")
        green1.write(0)
        green2.write(0)
        yel1.write(1)
        yel2.write(1)
        time.sleep(5)
        print("STOP")

while True:
    hours = time.time() / 3600
    hour = hours % 24
    
    if num == 1:
        num=0
    else:
        num=1
    #street A is usually busier, so from 15-18 and 6-9, the light is longer for it 
    if hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour==10 or hour==11 or hour==12 or hour==13 or hour==14 or hour==15 or hour==19 or hour==20 or hour==21 or hour==22 or hour==23:
        reghours()
    else:
        rushhours()
