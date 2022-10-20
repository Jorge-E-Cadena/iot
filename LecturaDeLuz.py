import machine
import utime

buttonOne = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

greenLed = machine.Pin(2, machine.Pin.OUT)
yellowLed = machine.Pin(3, machine.Pin.OUT)
redLed = machine.Pin(4, machine.Pin.OUT)

lightSensor = machine.ADC(26)
lightSensorLecture = lightSensor.read_u16()

lightRange = {
    'green': '7000',
    'yellow': '10000',
    'red': '65535'
}

while True:
    greenLed.value(1)
    if buttonOne.value()==1:
        greenLed.value(0)
        yellowLed.value(0)
        redLed.value(0)
        print("Iniciando medición de luz")
        while True:

            if lightSensorLecture < lightRange.get('green'):
                greenLed.value(1)
            elif lightSensorLecture >= lightRange.get('green') and lightSensorLecture < lightRange.get('yellow'):
                yellowLed.value(1)
            else:
                redLed.value(1)

            print(lightSensorLecture)
            utime.sleep(1)