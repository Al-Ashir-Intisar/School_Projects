import pyautogui

def locate_image():
    #pyautogui.click('minimize.PNG')
    cords_image = pyautogui.locateOnScreen('minimize.PNG')
    cords_center = pyautogui.center(cords_image)
    pyautogui.click(cords_center[0]+110, cords_center[1])
    print(cords_image, cords_center)


locate_image()