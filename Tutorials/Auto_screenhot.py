import pyautogui
import time

def test1():
    pyautogui.click(491,25)
    time.sleep(3)
    pyautogui.click(1073, 659)
    time.sleep(3)
    pyautogui.typewrite("youtube.com")
    pyautogui.press("enter")
    x=0
    while x<3:
        time.sleep(3)
        name = "photo"+str(x)+".png"
        pyautogui.screenshot(name)
        pyautogui.click(1910,1062)
        x= x+1

    #print(pyautogui.position())

test1()