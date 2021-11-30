import random

def compKwordAndSample(aikw,userkw) : 
    
    #ai스크립트 추출 키워드와 유저메인키워드의 차집합
    relatedKword = list(set(aikw) - set(userkw))
    # #5개 랜덤추출
    # sample5 = random.sample(relatedKword,5)

    return relatedKword

