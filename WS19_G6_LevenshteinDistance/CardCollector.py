import os
from Card import Card
from CardRepair import CardRepair

class CardCollector(object):
    #Class attributes

    def __init__(self):
        self.brokenCards = []
        self.referenceNames = []
        self.repairedCards = []

    #Builds cards from the parameter filename and writes them into self.brokenCards.
    #Parameters:
    #Opens a file from the parameter filename
    def buildScrambled(self, filename):

        #Preconditon
        assert(filename != None) 
        assert(len(self.brokenCards) == 0)

        relPath = "Files/" + filename + ".txt"
        file = open(relPath, "r+")

        for line in file:
            lineSplit = line.split("|")
            brokenCard = Card(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4])
            self.brokenCards.append(brokenCard)

        file.close()

        #Postcondition
        assert(file.closed) 
        assert(len(self.brokenCards) > 0)

    #Reads strings from the parameter filename and writes them into self.referenceNames.
    #Parameters:
    #Opens the relative path from the parameter file
    def buildReference(self, filename):
        #Precondition
        assert(filename != None) 
        assert(len(self.referenceNames) == 0)

        relPath = "Files/" + filename + ".txt"
        file = open(relPath, "r+")

        for line in file:
            self.referenceNames.append(str(line[:-2]))

        file.close()

        #Postcondition
        assert(file.closed)
        assert(len(self.referenceNames) > 0)

    #Writes the repairedCards into a selected path
    #Parameters:
    #path - create a new file at the given path
    def writeFile(self, path):
        assert(path != None) #Precondition
        assert(len(self.repairedCards) > 0) #Precondition

        file = open("Files/" + path + ".txt", "w+")
        for fixedCard in self.repairedCards:
            cardString = fixedCard.name + "|" + fixedCard.mana + "|" + fixedCard.cmc + "|" + fixedCard.type + "|" + fixedCard.count
            file.write(cardString)
        file.close()

        assert(file.closed) #Postcondition


    def getRepairedCardsList(self):
        for brokenCard in self.brokenCards:
            brokenCardName = brokenCard.name
            cardRepairObject = CardRepair(brokenCard, self.referenceNames)
            cardRepairObject.repair()
            if cardRepairObject.card.name is not brokenCardName:

                self.repairedCards.append(cardRepairObject.card)
