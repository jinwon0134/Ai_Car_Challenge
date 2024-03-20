from AltinoLite import *
Open()


def balance():
    if sensor.IR[4] > 15:
        steering(-80)
    elif sensor.IR[5] > 15:
        steering(80)
    else:
        steering(0)


def forward():
    steering(0)
    go(400,400)
    display('A')
    balance()

def bk():
    steering(0)
    go(0,0)

def turn_left():
    display('B')
    steering(-127)
    go(300,300)
    delay(800)
    while sensor.IR[3] > 10:
        # print(sensor.IR[1], sensor.IR[2], sensor.IR[3], sensor.IR[4], sensor.IR[5])
        if sensor.IR[3] < 30:
            steering(-127)
            go(400,400)
            delay(800)
        while sensor.IR[3] > 15:
            steering(127)
            go(-300,-300)
            if sensor.IR[6] > 100:
                break
    forward()




def turn_right():
    display('C')
    steering(127)
    go(300,300)
    delay(800)
    while sensor.IR[1] > 10:
        #print(sensor.IR[1], sensor.IR[2], sensor.IR[3], sensor.IR[4], sensor.IR[5])
        if sensor.IR[1] < 25:
            steering(127)
            go(400,400)
            delay(800)
        while sensor.IR[1] > 10:
            steering(-127)
            go(-300,-300)
            if sensor.IR[6] > 100:
                break
    forward()


while sensor.IR[5] < 300:
        delay(100)
count = 1
forward()
while True:
    #print(sensor.IR[1], sensor.IR[2], sensor.IR[3], sensor.IR[4], sensor.IR[5])
    if sensor.IR[2] > 17 or sensor.IR[1] > 40 or sensor.IR[3] > 40: 
        bk()
        print(sensor.IR[1], sensor.IR[2], sensor.IR[3], sensor.IR[4], sensor.IR[5])
        if sensor.IR[4] > sensor.IR[5]:
            steering(127)
            go(-300,-300)
            delay(900)
            turn_left()
        elif sensor.IR[4] < sensor.IR[5]:
            steering(-127)
            go(-300,-300)
            delay(900)
            turn_right()

            
    if sensor.CDS < 10:
        if count == 1:
            bk()
            sound(45)
            delay(1000)
            sound(0)
            count += 1
            forward()
        elif count == 2:
            bk()
            led(1)
            delay(1000)
            led(0)
            count += 1
            forward()
go(0,0)
