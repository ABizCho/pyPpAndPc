#####
import time as t
import datetime

#
import mod_myPyAutoGui as PAG
import mod_mainFunc as mf
import mod_userInput as userInput

import mod_choosen_NLP_extractKeyword_yake as ExKeyword
import mod_choosen_NLP_extractSessionKeyword_yake as ExSessKeyword
import mod_compAndSample_userKword_Aikword as compAndSampleKword
import mod_docxContentFraming as Framing
######


#스타트 메시지
mf.startMsg()


###### PROC1 사용자 input ######
mf.stepMsg(1,True)

sessionTopic = input('Type Your Main Topic : ')
sessionKeywordList = [] #사용자에게서 받는 모든 session keyword는 소문자로 작성하거나 / 소문자로 변경해야한다. : 파생원고로부터 연관키워드 선정 시 비교=>중복제거 수행예정

sessionKeywordList = userInput.userInput()

sessionKeyword = "{0}, {1}, {2}, {3}, {4}".format(sessionKeywordList[0],sessionKeywordList[1],sessionKeywordList[2],sessionKeywordList[3],sessionKeywordList[4])
print(sessionKeyword)


mf.stepMsg(1,False)
#################################





###### PROC2 ryte process #######
mf.stepMsg(2,True)

#1. rytr 오픈
PAG.win()
PAG.paste_in("rytr")
PAG.enter()

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
t.sleep(3)

#8.Make contents in rytr doc (repeat 4 time)
PAG.tab(13)
PAG.enter()
t.sleep(9)

PAG.tab(36)
PAG.enter()
t.sleep(9)

for i in range(3) :
    PAG.tab(13)
    PAG.enter()
    t.sleep(9)
    # clickCv.clickRyteMore()
    # t.sleep(8)


#9.copy the script
PAG.select_all()
PAG.copy()
script = clipboard.paste()
t.sleep(0.1)

PAG.quit()

mf.stepMsg(2,False)
##################################################


##### PROC3 연관키워드 선별,추출 using NLP #########
mf.stepMsg(3,True)


ai_related_kword = ExKeyword.keywordExtract_from_AIscript(script) # ai스크립트에서 추출된 연관키워드
user_kword = ExSessKeyword.makeComparedKeywordList(sessionKeywordList) # 유저인풋 메인키워드

sample_5relKW= compAndSampleKword.compKwordAndSample(ai_related_kword,user_kword) 


mf.stepMsg(3,False)
###################################################

###### PROC4 WORD파일 작성 #############
mf.stepMsg(4,True)


#1. word 오픈 & 새 문서
PAG.win()
PAG.paste_in('word')
PAG.enter()
t.sleep(4)

PAG.enter()
t.sleep(0.5)

#2. word작성
docxContent = Framing.framing_docx(sessionKeywordList,sessionTopic,sample_5relKW,script)
PAG.paste_in(docxContent)
t.sleep(0.1)

#3. 저장
PAG.save()

dateF = datetime.date.today().strftime("%y.%m.%d")
PAG.paste_in("조성우_영문원고작성({0})_{1}".format(dateF,sessionKeywordList[0]))
PAG.enter()
t.sleep(0.5)

PAG.quit()
t.sleep(0.5)

mf.stepMsg(4,False)
######################################


mf.finishMsg()




#================= Code made for paraphrasing version but discarded =============
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