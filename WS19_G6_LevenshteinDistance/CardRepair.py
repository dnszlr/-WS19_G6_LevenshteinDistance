class CardRepair(object):
    #description of class

    def __init__(self, card, allCards):
        assert card != None and allCards != None #Precondition
        self.card = card
        self.allCards = allCards

    #create the LD-matrix
    def LD(self, referenceName):
        assert len(self.card.name) >= 1 and  len(referenceName) >= 1
        cardRefName = list(self.card.name)
        cardScramName =list(referenceName)
        x = len(cardRefName)
        y = len(cardScramName)
        matrix = [[0 for i in range(y+1)] for i in range(x+1)]
        
        matrix[0][0] = 0
        for i in range(0, x+1):
            matrix[i][0] = i
        for j in range (0, y+1):
            matrix[0][j] = j
        
        for j in range(1, y+1):
            for i in range(1, x+1):
                c = 1
                if (self.card.name[i-1] is referenceName[j-1]) : 
                    c = 0
                rep = matrix[i-1][j-1] + c
                ins = matrix[i][j-1] + 1
                delete = matrix[i-1][j] + 1
                matrix[i][j] = min(rep, ins, delete)

        return matrix

    #repair the name of the card from the cards list
    def repair(self):
        #assert(brokenCard != None and allCards != None) #Precondition
        for i in range (len(self.allCards)):

            if((len(self.allCards[i]) -len(self.card.name)) >= -3 and (len(self.allCards[i]) -len(self.card.name)) <=3 ):

                repairMatrix = self.LD(self.allCards[i])
                #procentLen = 100 / len(brokenCard.name)
                #match = len(brokenCard.name) - repairMatrix[len(brokenCard.name)][len(allCards[i])] * procentLen
                match = (repairMatrix[len(self.card.name)][len(self.allCards[i])] * 100) / len(self.card.name)
                if(match <= 60):
                    j = repairMatrix[len(self.card.name)][len(self.allCards[i])]
                    x1 = len(self.card.name)
                    y1 = len(self.allCards[i])
                    while (j is not repairMatrix[0][0]):
                        northwest = repairMatrix[x1-1][y1-1]
                        west = repairMatrix[x1-1][y1]
                        north = repairMatrix[x1][y1-1]
                        rightCardName = self.allCards[i]
                        if min(northwest, north, west) is northwest:
                            self.replace(x1-1, self.allCards[i][y1-1])
                            x1 = x1 - 1
                            y1 = y1 - 1
                        elif min(northwest, north, west) is north:
                            self.insert(x1-1, self.allCards[i][y1-1])
                            y1 = y1 - 1
                        elif min(northwest, north, west) is west:
                            self.delete(x1-1);
                            x1 = x1 - 1
                        j = repairMatrix[x1][y1]
                    return self.card

        return self.card

    #inserts the letter c at the index i
    def insert(self, i, c):
        #assert(i >= 0) #Precondition
        self.card.name = self.card.name[:i] + c + self.card.name[i:]
        #assert(self.card.name[i] == c) #Postcondition (Letter c ist an index i)

    #deletes the letter at the index i
    def delete(self, i):
        #assert(i >= 0) #Precondition
        self.card.name = self.card.name[0 : i :] + self.card.name[i + 1 : :]
        #assert() #Postcondition (Alte Wortlaenge - 1)

    #replaces the letter at index i with c.
    def replace(self, i, c):
        #assert(i >= 0) #Precondition (Letter c ist an index i)
        self.card.name = self.card.name[:i] + c + self.card.name[i + 1:]
