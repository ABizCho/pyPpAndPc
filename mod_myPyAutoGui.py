import pyautogui
import time
import clipboard

#WINDOW MENU
def win() :
    pyautogui.press('win')
    time.sleep(1)

#PASTE in window menu
def paste_win(S) :
    clipboard.copy(S)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    
    pyautogui.press('enter')
    time.sleep(6)

#TAB key n time
def tab(n) :
    for i in range(n) :
        time.sleep(0.05)
        pyautogui.press('tab')

#PASTE in chrome
def search_chrome(S) :
    clipboard.copy(S)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4)