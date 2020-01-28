#!/usr/bin/python3
'''MIT (C), Aayush'''

import subprocess
from time import sleep
from os import system, getenv

ifttapi = getenv("IfttKey")
cmd = "acpi" 


sent = False

def checkBattery():
    p = subprocess.run(cmd, shell=True, capture_output=True)
    battery_info, error = p.stdout.decode(), p.stderr.decode() 
    if not error:
        batt = battery_info.split()[3]
        batt = batt[:-2]
        batt = int(batt)
        if batt < 40:
            if not sent:
                #could have turned of the switch but i'd rather save my smart switch and use it with my lamp
                system("notify-send 'Battery is under 40%'")
                system(f"curl -X POST https://maker.ifttt.com/trigger/laptopBatterlyLow/with/key/{ifttapi}")







checkBattery()
