#####
import pyautogui
import time
#
import md1_userInput

#####

#####사용자 입력
input("give me keyword :")
#####

#####스크래핑
#####

#####문자열 전처리
#####

#####패러프레이징
###
pyautogui.press('winleft')
#
time.sleep(0.4)
pyautogui.typewrite('quillbot',interval=0.1)
pyautogui.press('enter')
time.sleep(6)
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

###
pyautogui.hotkey('ctrl','t')
time.sleep(3)

pyautogui.typewrite('www.',interval=0.1)
pyautogui.press('enter')
time.sleep(6)
###
#####

#####export & save in hangeul

#####
