#YAKE를 이용한 NLP - keyword extracting

    #REF : https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c

import yake
kw_extractor = yake.KeywordExtractor()


def keywordExtract_from_AIscript(text) :

    language ="en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords,features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    # for kw in keywords:
    #     print(kw)

    
    KList = list(map(list,keywords))
    KL = list(KList)
    tempKL = list(KL)

    for i in range(len(keywords)) :
        
        #연관성이 0.01 이상인 키워드만생존
        KList[i][0] = keywords[i][0].lower()
        if KList[i][1] <= 0.02 :
            KL.remove(KList[i])
        
        #두 단어의 합성어 키워드만 생존
        sp = ' '
        if sp not in tempKL[i][0] :
            KL.remove(tempKL[i])

    

    print(KL)
    return KL

# #Test Code
# script = "California's Great America, commonly known simply as Great America, is a 112-acre (45 ha) amusement park[1] located in Santa Clara, California. Owned and operated by Cedar Fair, it originally opened in 1976 as one of two parks built by the Marriott Corporation. California's Great America features over 40 rides and attractions, and one of its most notable is Gold Striker, which has been featured as a top-ranked wooden roller coaster in Amusement Today's annual Golden Ticket Awards publication. Other notable rides include RailBlazer, a single-rail coaster from Rocky Mountain Construction, and Flight Deck, an inverted coaster from Bolliger & Mabillard. The park appeared in Beverly Hills Cop III and Getting Even with Dad, two films that were released in 1994."

# a = keywordExtract_from_AIscript(script)
# # 선정된 연관 키워드 소문자화 필요 : 원고작성에 사용된 session keyword와 비교하여 동일한 키워드는 연관키워드 목록에서 제거 해야하기 때문이다.