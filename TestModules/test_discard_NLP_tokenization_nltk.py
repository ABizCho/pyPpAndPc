# #from nltk.tokenize import word_tokenize


# #모든 사용자입력 session keyword는 소문자로 작성돼야한다. : yake로 선정된 ai원고 연관키워드와의 비교에 사용되기 때문에 소문자로 통일시킨다.

# from nltk.tokenize import TreebankWordTokenizer
# tokenizer = TreebankWordTokenizer()


# #계획 : process1의 사용자 입력에서 등장한 'session keyword : 합성어 키워드'를 아래와 같이 분해시킬 예정.
#     # 기존의 분해되기 전 session keywords와 아래에서 분해된 개별 단어들을 모두 comparedKeywordList에 저장한다.
#     # + 최소단위로 분해시킨 각 word를 위에 저장된 키워드를 제외시키고 모든경우의 수로 조합하여, comparedwordList에 저장한다.
#     # yake를 이용해서 proc2:rytr의 결과물인 ai원고에서 파생시킬 연관키워드를 선정할 때, comparedkeywordList와 비교하여 저장한다.
# def makeComparedKeywordList(sessionKwordList) :
#     comparedKwordList = []
    
#     for i in range(5) :
#         comparedKwordList.extend(tokenizer.tokenize(sessionKwordList[i]))
#     print(comparedKwordList)
    
#     return comparedKwordList #메인 process에서 comparedKeywordList로 받게 될 예정 


# ##구두점 제거
# #cleaned_sentence = sentence.replace('!', '').replace(',','').replace('.','').replace('“','').replace('”','').replace('\n','').replace('’','').replace(':','').replace('&','').#replace('(','').replace(')','').replace('[','').replace(']','').replace("'",'').replace('‘','')


# # #Tokenization
# # print(tokenizer.tokenize(sentence))
# # #print(word_tokenize(cleaned_sentence))

# #Test makeComparedKeywordList
# Test_inputKwordList = [] #사용자에게서 받는 모든 session keyword는 소문자로 작성하거나 / 소문자로 변경해야한다. : 파생원고로부터 연관키워드 선정 시 비교=>중복제거 수행예정
# for i in range(5) :
#     Test_inputKwordList.append(input('Type Your 5 keywords : '))

# Test_inputKwordList = "{0}, {1}, {2}, {3}, {4}".format(Test_inputKwordList[0],Test_inputKwordList[1],Test_inputKwordList[2],Test_inputKwordList[3],Test_inputKwordList[4])
# print(Test_inputKwordList)
# print(Test_inputKwordList)

# makeComparedKeywordList(Test_inputKwordList)



#+===================


import yake
kw_extractor = yake.KeywordExtractor()

language ="en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 20
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords,features=None)
# keywords = custom_kw_extractor.extract_keywords('script')
# for kw in keywords:
#     print(kw)


#def
def makeComparedKeywordList(sessionKwordList) : #input은 main의 sessionKeywordList가 들어갈 예정 (not var 'sessionKeyword')
    comparedKwordList = list()
    
    for skw in range(len(sessionKwordList)) :
        keywords = custom_kw_extractor.extract_keywords(sessionKwordList[skw])
        print(keywords)
        keywordList = list()
        
        for i in range(len(keywords)) :
            keywordList.append(keywords[i][0])
        comparedKwordList.extend(keywordList)

    return comparedKwordList

#test_input
Test_inputKwordList = []
for i in range(5) :
    Test_inputKwordList.append(input('Type Your 5 keywords : '))

#test
testresult = makeComparedKeywordList(Test_inputKwordList)
print(testresult)