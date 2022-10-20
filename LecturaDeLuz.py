import machine
import utime

buttonOne = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

greenLed = machine.Pin(2, machine.Pin.OUT)
yellowLed = machine.Pin(3, machine.Pin.OUT)
redLed = machine.Pin(4, machine.Pin.OUT)

lightSensor = machine.ADC(26)
lightSensorLecture = lightSensor.read_u16()

lightRange = {
    'green': 16375,
    'yellow': 32750,
    'red': 65535
}

while True:
    greenLed.value(1)
    yellowLed.value(0)
    redLed.value(0)
    if buttonOne.value()==1:
        greenLed.value(0)
        yellowLed.value(0)
        redLed.value(0)
        print("Iniciando medición de luz")
        while True:

            if lightSensor.read_u16() < lightRange.get('green'):
                greenLed.value(1)
                yellowLed.value(0)
                redLed.value(0)
            elif lightSensor.read_u16() >= lightRange.get('green') and lightSensor.read_u16() < lightRange.get('yellow'):
                greenLed.value(0)
                yellowLed.value(1)
                redLed.value(0)
            else:
                greenLed.value(0)
                yellowLed.value(0)
                redLed.value(1)

            print(lightSensor.read_u16())
            utime.sleep(1)
