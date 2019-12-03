import os
from Card import Card

class CardCollector(object):
    #Class attributes

    def __init__(self):
        self.brokenCards = []
        self.referenceNames = []
        self.repairedCards = []

    def readFile(self, path):
        assert(path != None) #Precondition

        relPath = "Files/" + path + ".txt"
        file = open(relPath, "r+")
        #assert(file != None) #Postcondition
        #file.close()
        return file

    #Builds cards from the parameter file and writes them into a self.brokenCards.
    def buildScrambled(self, file):
        assert(file != None) #Preconditon

        for line in file:
            lineSplit = line.split("|")
            brokenCard = Card(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4])
            self.brokenCards.append(brokenCard)

        assert(len(self.brokenCards) > 0) #Postcondition

    #Reads strings from the parameter file and writes them into a list.
    #Returns a new list with cards
    def buildReference(self, file):
        assert(file != None) #Precondition

        for line in file:
            self.referenceNames.append(str(line))

        assert(len(self.referenceNames) > 0) #Postcondition

    #Writes the repairedCards into a selected path
    #Parameters:
    #path - create a new file with the given path
    def writeFile(self, path):
        assert(path != None) #Precondition

        file = open("Files/" + path + ".txt", "w+")
        for fixedCard in self.repairedCards:
            cardString = fixedCard.name + "|" + fixedCard.mana + "|" + fixedCard.cmc + "|" + fixedCard.type + "|" + fixedCard.count
            file.write(cardString)
        file.close()

        #assert(len(f.readline) > 0) #Postcondition






