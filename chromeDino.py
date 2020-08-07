import pyautogui as p
from PIL import Image, ImageGrab
import time

def click(key):
    p.keyDown(key)
    time.sleep(0.5)  ## time is alloted to switch to chrome screen 
    p.keyUp(key)
    return

def isCollision(data):
#check collision for birds
    for i in range(690,730):
        for j in range(260,285):
            if data[i, j] < 171:
                click("down")
                return
 # Check colison for cactus
    for i in range(690,740):
        for j in range(310,340):
            if data[i, j] < 100:
                click("up")
                return
    return


if __name__=="__main__":
    print('Beginning in just 5 seconds.......Switch to chrome screen!!')
    time.sleep(5)
    click('up')
while True:
    image=ImageGrab.grab().convert('L')
    data=image.load() 
    isCollision(data)
    '''
    #for birds
    for i in range(690, 730):
        for j in range(280,305):
            data[i,j]=171
    #for cactus
    for i in range(690, 740):
        for j in range(310,340):
            data[i,j]=0
    image.show()
    break
    '''

