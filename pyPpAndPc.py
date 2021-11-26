#####
import pyautogui
import clipboard    #pyautogui를 이용한 타이핑시 한/영 문제 대안으로 os클립보드 제어
import time
#
import mod_myPyAutoGui as PAG
import proc1_userInput as proc1_input

savedStr = str()

#####

#####사용자 입력
keywords = proc1_input.userInput()
#
print(keywords)                 #TEST CODE
#
time.sleep(0.5)
#####



#####스크래핑
PAG.win()
PAG.paste_win('chrome')

#####

#####문자열 전처리
#####

#####패러프레이징
###
pyautogui.press('winleft')
#
time.sleep(0.4)
clipboard.copy('quillbot')
pyautogui.hotkey('ctrl','v')
time.sleep(0.5)
#
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
pyautogui.hotkey('ctrl','v')
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



##### finish message 
print("===============The end==================")
#####