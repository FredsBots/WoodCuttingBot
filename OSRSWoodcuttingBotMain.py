import pyautogui
import time
import random
############### Functions ###################

### oak logs ###
def oakDraynor():
    randomNum = random.uniform(0.5,2.0)
    exrand = random.uniform(15,21)
    clicks = random.uniform(9.5,10.3)

    pyautogui.moveTo(932,530,duration=randomNum)
    pyautogui.click(button="left")

    
    pyautogui.moveTo(909,531,duration=randomNum)
    pyautogui.click(button="left")

    time.sleep(0.2)

    banking()

    pyautogui.moveTo(1116,558,duration=randomNum)
    pyautogui.click(button="left")
    time.sleep(9.5)
    
    for asd in range(19):
        pyautogui.moveTo(955,530,duration=randomNum)
        pyautogui.click(button="left")        #Clicks on oak tree
        time.sleep(exrand)

    pyautogui.moveTo(761,490,duration=randomNum)
    pyautogui.click(button="left")

    time.sleep(clicks)

def contOak():
    try:
        while True:
            oakDraynor()
    except KeyboardInterrupt:
        print("\nDone")
        quit()
################
def start():
    setUpTimer()
    contOak()

def setUpTimer():
    txt = "You have 5 seconds to move this off your screen"
    print(txt)
    for y in range(6,0,-1):
        print(y-1,end="\r")
        time.sleep(1)
        
def banking():
    randomNum = random.uniform(0.5,1.0)
    print("depositing items")
    pyautogui.moveTo(1014,728,duration=randomNum)
    pyautogui.click(button="left")
    time.sleep(0.5)
    print("closing bank")
    pyautogui.moveTo(1081,60,duration=randomNum)
    pyautogui.click(button="left")
################################### Main Program #######################################
start()
