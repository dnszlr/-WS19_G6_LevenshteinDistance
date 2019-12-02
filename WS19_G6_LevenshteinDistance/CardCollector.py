import os
from Card import Card

class CardCollector(object):
    #Class attributes

    def __init__(self):
        self.brokenCards = []
        self.referenceNames = []
        self.repairedCards = []

    def read(self, path):
        assert(path != None) #Precondition

        relPath = "../WS19_G6_LevenshteinDistance/Files/" + path + ".txt"
        textFile = open(relPath, "r")

        assert(textFile != None) #Postcondition
        return textFile

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
    def write(self, path):
        assert(path != None) #Precondition

        file = open("../WS19_G6_LevenshteinDistance/Files/" + path + ".txt", "a")
        for fixedCard in self.repairedCards:
            cardString = fixedCard.name + fixedCard.mana + fixedCard.cmc + fixedCard.type + fixedCard.count
            file.append(cardString)

        assert(len(file.readline) > 0) #Postcondition






