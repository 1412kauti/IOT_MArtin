from gpiozero import LED,MotionSensor,LEDBoard
from time import sleep
from signal import pause

blue_led = LED(7)
pir_led = LED(23)
pir_sensor = MotionSensor(18)
fan_sensor = LED(4)
led_seq = LEDBoard(13,19,26,16,20,21)

single_led_status = False
pir_status = False
fan_status = False
led_seq_status = False

def single_LED_start():
    single_led_status = True
    if single_led_status == True:
        blue_led.value = 1
def single_LED_stop():
    single_led_status = False
    if single_led_status == False:
        blue_led.value = 0
def pir_start():
    pir_status = True
    if pir_status == True:
        pir_sensor.when_motion = pir_led.on
        pir_sensor.when_no_motion = pir_led.off
def pir_stop():
    pir_status = False
    if pir_status == False:
        pir_sensor.when_motion = pir_led.off
        pir_sensor.when_no_motion = pir_led.off
def fan_start():
    fan_status = True
    if fan_status == True:
        fan_sensor.value = 1
def fan_stop():
    fan_status = False
    if fan_status == False:
        fan_sensor.value = 0
def led_seq_start():
    led_seq_status = True
    if led_seq_status == True:
        led_seq.value = (1, 1, 1, 1, 1, 1)
        sleep(1)
        led_seq.value = (1, 1, 1, 0, 0, 0)
        sleep(1)
        led_seq.value = (0, 0, 0, 1, 1, 1)
        sleep(1)
        led_seq.value = (1, 0, 0, 0, 0, 0)
        sleep(1)
        led_seq.value = (1, 1, 1, 1, 1, 1)
        sleep(1)
def led_seq_stop():
    led_seq_status = False
    if led_seq_status == False:
            led_seq.value = (0, 0, 0, 0, 0, 0)
    
        