import subprocess
from time import sleep
from os import system, getenv
from pyautogui import hotkey


notified = False
ifKey = getenv("iftt_API_KEY")

def checkIfConnected():
    cmd = "pmset -g batt"
    s = subprocess.run(cmd, shell=True, capture_output=True)
    s = s.stdout.split()[3].decode()[1:]

    sleep(1)
    if s == "Battery":
        return False
    return True


def scream():
    global notified
    if not notified:
        system(f"curl https://maker.ifttt.com/trigger/\macbook_unplugged\/with/key/{ifKey}")
        system("say 'let go let go let go'")
        system("say 'i have notified the owner, he will be back soon'")
        system("babe ping phone"). #this is a seperate python custom file (you can delete this)
    system("say 'plug me back in'")
    notified = True


def main():
    if not checkIfConnected():
        print("Plug the macbook first")
        exit()
    hotkey("ctrl", "command", "q")
    while True:
        if not checkIfConnected():
            scream()


if __name__ == "__main__":
    try:
        main()
    except:
        exit("\nBye")
