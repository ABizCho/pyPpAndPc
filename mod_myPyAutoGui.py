import pyautogui
import time
import clipboard

#WINDOW MENU
def win() :
    pyautogui.press('win')
    time.sleep(1)

#PASTE in instant empty (short term)
def paste_in(S) :
    clipboard.copy(S)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)

#PASTE in window menu and enter (long term)
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

#PASTE a string in chrome
def search_chrome(S) :
    clipboard.copy(S)

    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4)

###### SIMPLE PRESS & HOTKEY ######

#Enter pressing
def enter() :
    pyautogui.press('enter')

#Del pressing
def delete() :
    pyautogui.press('del')

#Copy simple hotkey
def copy() :
    pyautogui.hotkey('')

#Quit(alt f4) simple hotkey
def quit() :
    pyautogui.hotkey('')

#Select All charactors simple hotkey
def select_all() :
    pyautogui.hotkey('ctrl','a')

##########################



