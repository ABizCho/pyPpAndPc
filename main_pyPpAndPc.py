#####
import pyautogui
import clipboard    #pyautogui를 이용한 타이핑시 한/영 문제 대안으로 os클립보드 제어
import time as t
import datetime
#
import mod_myPyAutoGui as PAG
import mod_mainFunc as mf
import proc1_userInput as proc1_input
######

###### 사용자 input
sessionTopic = input('Type Your Main Topic : ')
sessionKeyword = []
for i in range(5) :
    sessionKeyword.append(input('Type Your 5 keywords : '))

sessionKeyword = "{0}, {1}, {2}, {3}, {4}".format(sessionKeyword[0],sessionKeyword[1],sessionKeyword[2],sessionKeyword[3],sessionKeyword[4])
print(sessionKeyword)

mf.startMsg()

###### ryte
#1. rytr 오픈
PAG.win()
t.sleep(0.5)
PAG.paste_win('rytr')

#2. 기존 세션토픽 삭제
PAG.select_all()
PAG.delete()

#3.뉴 세션토픽 입력
PAG.paste_in(sessionTopic)

#4.세션키워드 박스로 이동
PAG.tab(1)

#5.뉴 세션키워드 삭제
PAG.select_all()
PAG.delete()

#6. 뉴 세션키워드 입력
PAG.paste_in(sessionKeyword)

#7. rytr 새문서 생성 및 오픈
PAG.tab(7)
PAG.enter()
t.sleep(0.5)

PAG.paste_in(str(datetime.date.today()))
PAG.enter()
t.sleep(1.5)

#8.Make contents in rytr doc (repeat 4 time)
Expand = "Expand"
for i in range(2) :
    PAG.paste_in(Expand)
    PAG.tab(13)
    PAG.enter()
    t.sleep(20)
    PAG.enter()
    t.sleep(0.1)

#9.ryte 3 time in the same way as step 8


#######







# savedStr = str()

# #####

# #####사용자 입력
# keywords = proc1_input.userInput()
# #
# print(keywords)                 #TEST CODE
# #
# time.sleep(0.5)
# #####



# #####스크래핑
# PAG.win()
# PAG.paste_win('chrome')


# #####

# #####문자열 전처리
# #####

# #####패러프레이징
# ###
# pyautogui.press('winleft')
# #
# time.sleep(0.4)
# clipboard.copy('quillbot')
# pyautogui.hotkey('ctrl','v')
# time.sleep(0.5)
# #
# pyautogui.press('enter')
# time.sleep(6)
# ###

# ###
# for i in range(13) :
#     pyautogui.press('tab')
# pyautogui.hotkey('ctrl','v')
# #
# time.sleep(3)
# pyautogui.hotkey('ctrl','enter')
# #
# time.sleep(20)
# for i in range(4) :
#     pyautogui.press('tab')
# pyautogui.hotkey('ctrl','a')
# #
# pyautogui.hotkey('ctrl','v')
# ###

# ###
# pyautogui.hotkey('ctrl','t')
# time.sleep(3)

# pyautogui.typewrite('www.',interval=0.1)
# pyautogui.press('enter')
# time.sleep(6)
# ###
# #####

# #####export & save in hangeul

# #####



# ##### finish message 
# print("===============The end==================")
# #####