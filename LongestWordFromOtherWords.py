'''
Created on May 25, 2014
@author: tanmaymehrotra
'''

def sortListOfWordsBylength(listOfWords):
    listOfWords.sort(key=len,reverse=True)
    return listOfWords

def longestWord(sortedListOfWords):
    wordsNotPresent = set()
    for word in sortedListOfWords:
        if checkIfWordIsPresent(word,word,sortedListOfWords,wordsNotPresent) == True:
            return word
    return "none of the words can be made from other words"    
        

def checkIfWordIsPresent(word,originalWord,sortedListOfWords,wordsNotPresent):
    if word in sortedListOfWords and word is not originalWord:
        return True
    for i in range(len(word)-1):
        leftpart = word[:i+1]
        rightpart = word[i+1:]
        if leftpart in sortedListOfWords and rightpart not in wordsNotPresent:
            wordIsPresent = checkIfWordIsPresent(rightpart,originalWord,sortedListOfWords,wordsNotPresent)
            if wordIsPresent == False:
                wordsNotPresent.add(word)
                return False
            else:
                return True
    return False
    
if __name__ == '__main__':
    listOfStrings = ["tan","works","at", "tanmaymehrotra","BofA","mehrotra"]
    print longestWord(sortListOfWordsBylength(listOfStrings))
    
    