#####
import pyautogui
import time
print(pyautogui.KEYBOARD_KEYS)

#####

#####스크래핑
#####

#####문자열 전처리
#####

###
pyautogui.press('winleft')
#
pyautogui.typewrite('quillbot',interval=0.1)
pyautogui.press('enter')
time.sleep(4)
###

###
for i in range(13) :
    pyautogui.press('tab')
pyautogui.hotkey('ctrl','v')
#
time.sleep(3)
pyautogui.hotkey('ctrl','enter')
#
time.sleep(20)
for i in range(4) :
    pyautogui.press('tab')
pyautogui.hotkey('ctrl','a')
#
pyautogui.press('ctrl','v')
###



#####export & save in hangeul

#####
