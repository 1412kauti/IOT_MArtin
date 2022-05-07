import pywebio
from pywebio.input import *
from pywebio.output import *
from functools import partial
import devices

def f1():
    devices.fan_start()
    toast("fan_on")
def f2():
    devices.fan_stop()
    toast("fan_off")
#def f3():
#    toast("camera_on")
#def f4():
#    toast("camera_off")
def f5():
    devices.single_LED_start()
    toast("led_on")
def f6():
    devices.single_LED_stop()
    toast("led_off")
def f7():
    toast("pir_on")
    devices.pir_start()
def f8():
    toast("pir_off")
    devices.pir_stop() 
def f9():
    toast("led_seq_on")
    devices.led_seq_start()
def f10():
    toast("led_seq_off")
    devices.led_seq_stop()



def serve_website():
    put_row([put_text("Martin's IOT Dashboard")])
    put_row([
        put_table([
            ['Fan',put_button(["ON"],onclick=f1),put_button(["OFF"],onclick=f2)],
            #['Camera',put_button(["ON"],onclick=f3),put_button(["OFF"],onclick=f4)],
            ['LED',put_button(["ON"],onclick=f5),put_button(["OFF"],onclick=f6)],
            ['PIR',put_button(["ON"],onclick=f7),put_button(["OFF"],onclick=f8)],
            ['LED Seq',put_button(["ON"],onclick=f9),put_button(["OFF"],onclick=f10)]
        ])
    ])

if __name__ == '__main__':
    pywebio.start_server(serve_website,port=80)
