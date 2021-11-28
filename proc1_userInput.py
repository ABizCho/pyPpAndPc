def userInput() : 
    numList = ['First','Second','Third','Fourth','Fifth']
    inputList = []

    for i in range(5) :
        inputList.append(input("Type your {0} keyword : ".format(numList[i])))
        
    return inputList
