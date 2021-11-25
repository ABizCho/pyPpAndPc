#####
import pyautogui
import time
print(pyautogui.KEYBOARD_KEYS)

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
for i in range(2) :
    pyautogui.press('tab')
pyautogui.press('enter')
#
pyautogui.press('tab')
pyautogui.hotkey('ctrl','a')
#
pyautogui.press('ctrl','v')
###



#####문자열 처리

#(1) 대괄호 등 제거 : 위키피디아용 제거

#####
