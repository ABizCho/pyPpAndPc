#from nltk.tokenize import word_tokenize


#모든 사용자입력 session keyword는 소문자로 작성돼야한다. : yake로 선정된 ai원고 연관키워드와의 비교에 사용되기 때문에 소문자로 통일시킨다.

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()


sentence = "Rockstar, Hype, Monster and Redbull are four of the most popular energy drink brands in the world. These drinks are often consumed by athletes and people who work for long hours to provide them with a boost of energy. Rockstar: Rockstar is one of the most popular energy drinks in the world. It has been endorsed by many famous artists such as Lil Wayne and Macklemore. It also sponsors many sporting events such as Ironman, NASCAR and Indycar races. Monster: Monster is one of the most popular energy drinks in the world with their slogan “Unleash The Beast” which is targeted at high-performance athletes. It also sponsors many sporting events such as Ironman, NASCAR and Indycar races. Rockstar energy drink is known for its high caffeinated content. It also contains taurine, guarana extract, and B vitamins. Hype energy drink is a low cost product with low sugar content. It also contains L-carnitine and ginseng extract. Monster energy drink is an iconic brand, famous for its catchy slogans like ‘Unleash the Beast’ and ‘Unleash your Inner Monster’. The ingredients of this product include glucose syrup, sodium citrate, sucrose syrup, carbonated water (carbon dioxide), natural & artificial flavors (contains milk), vitamin C (Ascorbic Acid), flavoring (contains milk), caffeine from guarana extract and natural flavors (contains milk)."

#구두점 제거
cleaned_sentence = sentence.replace('!', '').replace(',','').replace('.','').replace('“','').replace('”','').replace('\n','').replace('’','').replace(':','').replace('&','').replace('(','').replace(')','').replace('[','').replace(']','').replace("'",'').replace('‘','')

#명사 추출

print(word_tokenize(cleaned_sentence))



