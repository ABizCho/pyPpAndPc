def startMsg() :
    print("Thanks I'll make that===============")
def finishMsg() :
    print("Finish I've made that===============")

def stepMsg(stepnum,startORfinish) :
    status = 0
    if startORfinish == True :
        status = "Start"
    elif startORfinish == False :
        status = "Finished"
    print('<PROC{0}> [{1}] process..'.format(stepnum,status))
