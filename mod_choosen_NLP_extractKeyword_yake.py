#YAKE를 이용한 NLP - keyword extracting

    #REF : https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c

import yake
kw_extractor = yake.KeywordExtractor()
import string

def keywordExtract_from_AIscript(text) :

    language ="en"
    max_ngram_size = 3
    deduplication_threshold = 0.3
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords,features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    # for kw in keywords:
    #     print(kw)

    
    KList = list(map(list,keywords))
    KL = list(KList)
    tempKL = list(KL)

    for i in range(len(keywords)) :
        
        # #연관성이 0.01 이상인 키워드만생존
        # KList[i][0] = keywords[i][0].lower()
        # if KList[i][1] <= 0.0005 :
        #     KL.remove(KList[i])
   
        #두 단어의 합성어 키워드만 생존
        sp = ' '
        if sp not in tempKL[i][0] :
            KL.remove(tempKL[i])


    #생존한 연관키워드 리스트에서 연관성 지표를 버리고, 1차원 리스트로 재구성 ( 기존 세션키워드와 비교를 위해서 ) 
    for i in range(len(KL)) : 
        KL[i] = KL[i][0]

    for i in range(len(KL)) :
        KL[i] = KL[i].lower()
    return KL

# #Test Code
# script = "There are many different types of ovens in the market. Clay ovens are a good option for outdoor cooking because they can get very hot and their temperatures can be easily controlled. Dutch oven bread is a type of bread that is cooked in a clay or cast iron pot over an open fire, typically outdoors. Ribs in the oven is a type of slow-cooked meat dish wherein pork ribs are cooked by roasting them for a long time at low heat. Outdoor pizza oven is an insulated, outdoor-fired brick or stone oven designed to cook pizzas, which have been traditionally baked in clay or stone pots since Antiquity. This article will give you a brief overview on different types of ovens, their uses and how they work.A clay oven is one of the oldest ovens that are still in use. It works by using heated stones to create plenty of hot air, which then emits heat into the room.Dutch oven bread is baked in a dutch oven. The bread is put on parchment paper or placed directly on the dutch oven lid to collect all of the steam and moisture that comes out of the bread as it bakes. Ribs are traditionally cooked in an outdoor pizza oven because it has two racks for ribs and also has a metal dome so smoke stays inside the cooking chamber instead of being released into the atmosphere. Outdoor pizza ovens are a great option if you want to have a cooking experience that is close to what you would have in Italy. They are perfect for cooking pizzas, breads, and ribs.Know which one suits your needs from the list of ovens given below:1. Clay oven - It is best used in the winter when it can maintain a steady temperature up to 350 degrees Fahrenheit or 177 degrees Celsius.2. Dutch oven bread - This type of bread can be made by baking bread in an enclosed pot that has been either buried or sunk into coals and embers for an extended period of time. 3. Ribs in the oven - This refers to the process of roasting ribs inside an oven by using high temperatures and low moisture Ovens come in all shapes and sizes. Some are for outdoor use, some are for indoor use and some are multitaskers. Clay ovens provide a perfect environment to cook your food with high heat and without drying out the food. Dutch oven bread is an example of baking in a clay oven. Indoor ovens can be used with any type of cooking method, including baking, roasting, boiling and frying. Ribs in the oven would be an example of this type of cooking method done in an indoor oven.Outdoor pizza ovens allow you to cook pizza by placing the dough directly on the grill or directly on the stone that is heated by gas or wood."

# a = keywordExtract_from_AIscript(script)
# print(a)
# # 선정된 연관 키워드 소문자화 필요 : 원고작성에 사용된 session keyword와 비교하여 동일한 키워드는 연관키워드 목록에서 제거 해야하기 때문이다.