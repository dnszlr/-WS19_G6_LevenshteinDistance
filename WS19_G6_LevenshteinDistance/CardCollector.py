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

        relPath = "C:/Users/denni/source/repos/WS19_G6_LevenshteinDistance/WS19_G6_LevenshteinDistance/Files/reference.txt" #"../WS19_G6_LevenshteinDistance/Files/" + path + ".txt"
        f = open(relPath, "r+")
        assert(f != None) #Postcondition
        f.close()
        return f

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

        f = open(path, "w+")
        #open("../WS19_G6_LevenshteinDistance/Files/" + path + ".txt", "rb")
        for fixedCard in self.repairedCards:
            cardString = fixedCard.name + fixedCard.mana + fixedCard.cmc + fixedCard.type + fixedCard.count
            f.write(cardString)

        f.close()

        #assert(len(f.readline) > 0) #Postcondition






