#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Eny sample Blink GPIO LED on Raspberry PI """

from __future__ import print_function
import argparse
import serial
import sys
import time
import RPi.GPIO as GPIO
import eny
from gpiozero import LED

global flag, flag2, flag3
flag = flag2 = flag3 = 0
def main():
    """main"""
    
    if not sys.platform.startswith('linux'):
        raise EnvironmentError('Unsupported platform')

    parser = argparse.ArgumentParser(description='Samlle blink')
    parser.add_argument(
        '--pin',
        type=int,
        default=22,
        help='GPIO pin to LED+'
    )
    args = parser.parse_args()
    led_pin = args.pin

    parser = argparse.ArgumentParser(description='Samlle blink')
    parser.add_argument(
        '--pin',
        type=int,
        default=23,
        help='GPIO pin to LED+'
    )
    args = parser.parse_args()
    #led_pin2 = args.pin    
    led_pin2 = LED(23)
    led_pin3 = LED(27)

    def blink(eny_obj):
        """Blink LED"""
        print(eny_obj)
        global flag, flag2, flag3
        if eny_obj.id == "F0000016":
            if flag==1:
                GPIO.output(led_pin, GPIO.HIGH)
                flag = 0
                #time.sleep(0.5)
            else:
                GPIO.output(led_pin, GPIO.LOW)
                flag = 1

        if eny_obj.id == "F0000013":
            if flag2==1:
                #GPIO.output(led_pin2, GPIO.HIGH)
                led_pin2.on()
                flag2 = 0
                #time.sleep(0.5)
            else:
                led_pin2.off()
                flag2 = 1
        if eny_obj.id == "F000003D":
            if flag3==1:
                #GPIO.output(led_pin2, GPIO.HIGH)
                led_pin3.on()
                flag3 = 0
                #time.sleep(0.5)
            else:
                #GPIO.output(led_pin2, GPIO.LOW)
                led_pin3.off()
                flag3 = 1

    def blink_twice(eny_obj):
        """Blink LED twice"""
        print(eny_obj)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(led_pin, GPIO.LOW)

    # start GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)

    port = eny.get_port_names()[0]
    with serial.Serial(port, 115200) as uart:
        # eny.handle_click(uart, blink)
        eny.handle_double_click(uart, blink, blink_twice)
        uart.close()

    GPIO.cleanup()

if __name__ == '__main__':
    main()
