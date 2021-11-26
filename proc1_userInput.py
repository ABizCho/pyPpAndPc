
def userInput() : 
    numList = ['first','second','third','fourth','fifth']
    inputList = []

    for i in range(5) :
        inputList.append(input("type your {0} keyword : ".format(numList[i])))

    return inputList
