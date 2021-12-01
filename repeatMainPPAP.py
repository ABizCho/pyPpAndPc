#import main_pyPpAndPc as PPAP
import docx
import datetime
import time
import main_pyPpAndPc as PPAP



#####
TD = datetime.datetime.now().strftime("%y%m%d")
print(TD)
templ = docx.Document("C:\\Users\\JSW\\Desktop\\ppapResult\\keywords_{0}.docx".format(TD))

keywordBundleList = list()
for x, paragraph in enumerate(templ.paragraphs):
    keywordBundleList.append(paragraph.text)
    
if len(keywordBundleList) % 5 != 0 :
    for i in range(5 - len(keywordBundleList) % 5) :
        keywordBundleList.append('')

print(len(keywordBundleList))
L=len(keywordBundleList)//5
# KBL = list()
# for i in range(L) :
#     KBL = KBL.append([])
    
KBL = [[0 for j in range(5)] for i in range(L)]


for i in range(len(keywordBundleList)):
    KBL[i//5][i%5] = keywordBundleList[i]





#####
print("<<< Topic Series Process.. >>>")
MainTopicList = list()
for i in range(len(KBL)) :
    tempTopic = str()
    print("=======================")
    print("{0}\n{1}\n{2}\n{3}\n{4}\n".format(KBL[i][0],KBL[i][1],KBL[i][2],KBL[i][3],KBL[i][4]))
    MainTopicList.append(input("Let me know proper Topic.. : "))
    print("=======================")
    
print("=============<<< Thanks I'll operate main procs >>>=============")

for i in range(len(MainTopicList)) :
    PPAP.ppap(MainTopicList[i],KBL[i])
    time.sleep(2)

print("=============<< ALL process have finished >>====================")



