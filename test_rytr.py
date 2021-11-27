###
import pyautogui
import time as t
#
import mod_myPyAutoGui as PAG
###

1
PAG.win()
t.sleep(0.3)
PAG.paste_win('rytr')

#2
PAG.tab(3)
PAG.enter()
t.sleep(3.5)

try : 
    #3 이미지 인식으로 크롬 Buster 실행
    iconbtn = pyautogui.locateOnScreen("ster.png",confidence=0.9,grayscale=True) #인식할 buster icon.png
    print(iconbtn)
    center = pyautogui.center(iconbtn) #icon.png 센터값 구하기
    pyautogui.click(center)  # 이미지 클릭

    #문제발생 : buster 다회 시행시 리캡챠가 감지 (해결요망)
finally : 

    #4 
    PAG.tab(8)
    PAG.enter()
    t.sleep(1.5)

    PAG.tab(2)
    PAG.enter()
    t.sleep(4)