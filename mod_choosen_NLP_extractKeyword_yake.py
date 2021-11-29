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
    return KL

#Test Code
script = "A clay oven is a circular hole dug in the ground and then lined with bricks and heated from below by wood or coal fires. They were more common in ancient times and are still used for cooking traditional foods like pizza, bread, and ribs.A dutch oven is a deep pot with a heavy lid that can be used as an oven. It can be used to bake meat dishes such as meatloaf or roasts including beef, lamb, pork, fowls, game animals such as deer or rabbit. Ovens are also used for baking cakes such as cheesecake and pies such as apple pie.Clay ovens,Clay ovens were used in Japan, China, and Thailand before they were taken to Europe during the 17th century. It is a type of vernacular architecture that is made from natural materials such as clay, straw, earth, and stones. They are usually built outdoors in a similar way to an igloo or shelter. The cooking process is different from traditional ovens in that the inside of the oven remains cool with a small fire at the bottom which heats up air in a chimney stack. This hot air circulates throughout the structure cooking food evenly and slowly.’An oven is a thermally insulated chamber that is used for the heating, baking or drying of a substance, typically food.Different types of ovens are available in the market. Some are clay ovens which are mostly found in Italy. These are constructed by hand and are made to be fired with wood fire. Dutch oven bread is baked in this type of traditional oven. Outdoor pizza oven can be found in many restaurants these days because it produces crispy crust pizza which tastes much better than regular pizza that is made in an indoor brick or electric oven. Power air fryer oven can cook food very quickly without using any oil unlike other methods like frying, baking etc. The oven is an indispensable kitchen appliance that can be used for various purposes. There are plenty of ovens available in the market, each with its own set of features and functions.One type of oven is the clay oven which is usually found in traditional brick homes. The Dutch oven bread is often prepared in these types of ovens because they produce a crispy crust and soft inside which you won't find in any other type of oven.The outdoor pizza oven, on the other hand, uses brick to cook pizzas at high temperatures. This method allows people to cook pizzas quickly, without heating up their home or getting too much heat on the pizza itself. There are also power air fryer ovens which use convection cooking methods to cook food without adding fat or grease whatsoever.—The oven is a kitchen appliance that cooks food by applying heat. The oven was invented around the 1800s and since then, many different types of ovens have been created. This section will talk about clay oven, dutch oven bread, outdoor pizza oven, power air fryer oven and ribs in the oven.In this article, we dealt with 'Various ovens and oven Brands'. Next time, I'll come back with a better article. Thanks for reading & Warmest regards"

keywordExtract_from_AIscript(script)
# 선정된 연관 키워드 소문자화 필요 : 원고작성에 사용된 session keyword와 비교하여 동일한 키워드는 연관키워드 목록에서 제거 해야하기 때문이다.