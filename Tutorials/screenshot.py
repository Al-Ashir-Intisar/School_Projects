import pyautogui
import PIL
import time
def sh():
    pyautogui.click(931,1841)
    x = 0
    while x<680:
        a = 'sh' + str(x)+'.png'
        pyautogui.screenshot(a)
        pyautogui.click(786,1920)
        time.sleep(1.7)
        x = x+1

#pyautogui.click(1339, 49)
#pyautogui.screenshot('sh1.png')
#print(pyautogui.position())
#print(pyautogui.size())
sh()