import pyautogui as p
from time import sleep

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