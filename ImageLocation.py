import pyautogui
import time


def locating_image():
    pyautogui.click('minimize.PNG')
    time.sleep(0.1)
    chrome_Chords = pyautogui.locateOnScreen('chrome03.PNG')
    print(chrome_Chords)
    center_cords = pyautogui.center(chromeChords)
    pyautogui.doubleClick(chromeChords)
    time.sleep(2)
    pyautogui.click('maximize01.PNG')


def youtube_ss():
    pyautogui.click(1058, 700)
    time.sleep(2)
    pyautogui.typewrite("youtube.com")
    pyautogui.press("enter")
    x = 0
    while x < 5:
        time.sleep(3)
        name = "photo" + str(x) + ".png"
        pyautogui.screenshot(name)
        pyautogui.click(1910, 1062)
        x = x + 1


def main():
    locating_image()
    #youtube_ss()


main()