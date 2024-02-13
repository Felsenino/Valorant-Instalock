import pyautogui as p
from time import sleep
import tkinter as tk
from tkinter import ttk

'''
# INSERT HERE THE NAME OF THE AGENT YOU WANT TO PLAY
USER_AGENT_SELECT = "iso"


# variables 
lockButtonX, lockButtonY = 960, 730 #Res must be, 1920x1080
agent = USER_AGENT_SELECT.lower()
imgLocation = None
imageFile = f'imgs/{agent}.png'

# when pyautogui finds the image of the agents, returns the coordinates to imgLocation
while (imgLocation == None):
    try:
        imgLocation = p.locateCenterOnScreen(imageFile, confidence=0.8)
    except Exception as e:
        print(e)


p.moveTo(imgLocation)
p.click()
sleep(0.01)

p.moveTo(lockButtonX, lockButtonY)
p.click()

'''

# Bug, once you choose your agent, and it lock-in, DO NOT CHANGE SELECTION, if you do, program will crush, close it instead


# debug function
def log():
    print("True")


def selected(event):

    # INSERT HERE THE NAME OF THE AGENT YOU WANT TO PLAY
    #USER_AGENT_SELECT = "iso"


    # variables 
    lockButtonX, lockButtonY = 960, 730 #Res must be, 1920x1080
    #agent = USER_AGENT_SELECT.lower()
    agent = selector.get()
    print("Current agent selected:",agent)
    imgLocation = None
    imageFile = f'imgs/{agent}.png'

    # when pyautogui finds the image of the agents, returns the coordinates to imgLocation
    while (imgLocation == None):
        try:
            imgLocation = p.locateCenterOnScreen(imageFile, confidence=0.8)
        except Exception as e:
            print(e)


    p.moveTo(imgLocation)
    p.click()
    #sleep(0.01)

    p.moveTo(lockButtonX, lockButtonY)
    p.click()


# window cfg
window = tk.Tk() 
window.geometry("475x25")
window.title("Valorant Instalocker v0.2 by Felsen")
window.resizable(False, False)
window.configure(background="black")

# selector
agents = [
    "astra",
    "breach",
    "brimstone",
    "chamber",
    "cypher",
    "deadlock",
    "fade",
    "gekko",
    "harbor",
    "iso",
    "jett",
    "kayo",
    "killjoy",
    "neon",
    "omen",
    "phoenix",
    "raze",
    "reyna",
    "sage",
    "skye",
    "sova",
    "viper",
    "yoru"
]

selector = ttk.Combobox(window, height=50, width=50,font=(25), values = agents)
selector.set("Pick your agent") # bug, can edit this text
selector.bind("<<ComboboxSelected>>", selected)
selector.pack()


window.mainloop()