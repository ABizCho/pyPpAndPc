# docx content framing 

def framing_docx(sessionkeywordlist,topic,relatedkeywordlist,script) :
    #헤더
    frame_mainKeywords = "메인 키워드: {0}".format(sessionkeywordlist[0][0].upper() + sessionkeywordlist[0][1:])
    frame_mainTopic = "제목: {0} {1}, {2}, etc.".format(topic,sessionkeywordlist[0],sessionkeywordlist[1],sessionkeywordlist[2])
    frame_relatedKeywords = "연관 키워드: {0}".format(sessionkeywordlist[0])
    for i in range(1,len(relatedkeywordlist)) :
        frame_relatedKeywords += ', ' + relatedkeywordlist[i]

    #본문
    frame_script = script
    #클로징
    frame_closing = "In this time, we dealt with '{0}'. Next time, I'll come back with a better information. Thanks for reading & Warmest regards".format(topic)

    main_frame = frame_mainKeywords + '\n' + frame_mainTopic + '\n' + frame_relatedKeywords + '\n\n' + frame_script + '\n\n' + frame_closing + '\n\n\n\n'

    return main_frame 