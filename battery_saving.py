from machine import Pin, deepsleep, wake_reason, DEEPSLEEP_RESET, Timer, PWM
import esp32
import time

PIN_ON_PWR = 34

power_button = Pin(PIN_ON_PWR, Pin.IN, Pin.PULL_UP)

system_on = True

if wake_reason() == DEEPSLEEP_RESET:
    print('Rob está de volta!')
    system_on = True

def turn_off_system():
    global system_on
    system_on = False
    print('Desligando Rob...')
    time.sleep(.4)
    esp32.wake_on_ext0(pin=power_button, level=esp32.WAKEUP_ANY_HIGH)
    deepsleep()

def check_power_button(timer):
    global system_on
    if power_button.value() == 1:
        if system_on:
            turn_off_system()

time.sleep(0.4)
power_timer = Timer(0)
power_timer.init(period=100, mode=Timer.PERIODIC, callback=check_power_button)

try:
    while True:
        if system_on:
            print('Rob está online!')
            time.sleep(1)
        else:
            time.sleep(1)
except KeyboardInterrupt:
    power_timer.deinit()

