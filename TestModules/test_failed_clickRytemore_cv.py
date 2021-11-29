###
import pyautogui
import time as t
#
import mod_myPyAutoGui as PAG
###


def clickRyteMore() :
    #3 이미지 인식으로 크롬 Buster 실행
    iconbtn = pyautogui.locateOnScreen("Ryte_more.png",confidence=0.8,grayscale=True) #인식할 buster icon.png
    print(iconbtn)
    center = pyautogui.center(iconbtn) #icon.png 센터값 구하기
    pyautogui.click(center)  # 이미지 클릭


