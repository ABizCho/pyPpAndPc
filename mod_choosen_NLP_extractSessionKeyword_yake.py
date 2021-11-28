#=======세션 키워드 Tokenization, extract by Yake
    #For comparing with 파생 연관키워드

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



# ######test success=======
# #test_input
# Test_inputKwordList = []
# for i in range(5) :
#     Test_inputKwordList.append(input('Type Your 5 keywords : '))
# #test
# testresult = makeComparedKeywordList(Test_inputKwordList)
# print(testresult)
# #========================
