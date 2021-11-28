#YAKE를 이용한 NLP - keyword extracting

    #REF : https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c

import yake
kw_extractor = yake.KeywordExtractor()
script = "Rockstar, Hype, Monster and Redbull are four of the most popular energy drink brands in the world. These drinks are often consumed by athletes and people who work for long hours to provide them with a boost of energy. Rockstar: Rockstar is one of the most popular energy drinks in the world. It has been endorsed by many famous artists such as Lil Wayne and Macklemore. It also sponsors many sporting events such as Ironman, NASCAR and Indycar races. Monster: Monster is one of the most popular energy drinks in the world with their slogan “Unleash The Beast” which is targeted at high-performance athletes. It also sponsors many sporting events such as Ironman, NASCAR and Indycar races. Rockstar energy drink is known for its high caffeinated content. It also contains taurine, guarana extract, and B vitamins. Hype energy drink is a low cost product with low sugar content. It also contains L-carnitine and ginseng extract. Monster energy drink is an iconic brand, famous for its catchy slogans like ‘Unleash the Beast’ and ‘Unleash your Inner Monster’. The ingredients of this product include glucose syrup, sodium citrate, sucrose syrup, carbonated water (carbon dioxide), natural & artificial flavors (contains milk), vitamin C (Ascorbic Acid), flavoring (contains milk), caffeine from guarana extract and natural flavors (contains milk)."

language ="en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 20
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords,features=None)
keywords = custom_kw_extractor.extract_keywords(script)
for kw in keywords:
    print(kw)

print(type(keywords[1]))
print(keywords[1][1])