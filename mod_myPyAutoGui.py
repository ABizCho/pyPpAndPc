import pyautogui
import time
import clipboard

# print(pyautogui.KEYBOARD_KEYS)

#PASTE in instant empty (short term)
def paste_in(S) :
    clipboard.copy(S)
    time.sleep(0.1)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)

#PASTE in window menu and enter (long term)
def paste_win(S) :
    clipboard.copy(S)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    
    pyautogui.press('enter')
    time.sleep(5)

#TAB key n time
def tab(n) :
    for i in range(n) :
        pyautogui.press('tab')
        time.sleep(0.05)

#PASTE a string in chrome
def search_chrome(S) :
    clipboard.copy(S)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4)

###### SIMPLE PRESS & HOTKEY ######

#WINDOW MENU pressing
def win() :
    pyautogui.press('win')
    time.sleep(1)

#Enter pressing
def enter() :
    pyautogui.press('enter')

#Del pressing
def delete() :
    pyautogui.press('del')

#Copy simple hotkey
def copy() :
    pyautogui.hotkey('ctrl','c')

#Quit(alt f4) simple hotkey
def quit() :
    pyautogui.hotkey('alt','f4')

#Select All charactors simple hotkey
def select_all() :
    pyautogui.hotkey('ctrl','a')

#Save simple hotkey
def save() :
    pyautogui.hotkey('ctrl','s')
    time.sleep(0.8)

##########################



