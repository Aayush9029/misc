import subprocess
from time import sleep
from os import system, getenv
from pyautogui import hotkey


notified = False

def checkIfConnected():
    cmd = "wttr.in/Brampton"
    s = subprocess.run(cmd, shell=True, capture_output=True)
    print(s.stdout)

checkIfConnected()
