class CardRepair(object):
    #description of class

    def __init__(self, card, allCards):
        assert card != None and allCards != None #Precondition
        self.card = card
        self.allCards = allCards
        self.matrix = [[]]

    #create the LD-matrix
    def LD(self, referenceCard):
        assert len(self.card.name) >= 1 and  len(referenceCard.name) >= 1
        cardRefName = list(self.card.name)
        cardScramName =list(referenceCard.name)
        x = len(cardRefName)
        y = len(cardScramName)
        self.matrix = [[0 for i in range(x+2)] for i in range(y+2)]
        
        self.matrix[0][0] = 0
        for i in range(0, x+1):
            self.matrix[i][0] = i
        for j in range (0, y+1):
            self.matrix[0][j] = j
        
        
        
        for j in range(1, y+1):
            for i in range(1, x+1):
                c = 1
                if (self.card.name[i-1] is referenceCard.name[j-1]) : 
                    c = 0
                rep = self.matrix[i-1][j-1] + c
                ins = self.matrix[i][j-1] + 1
                delete = self.matrix[i-1][j] + 1
                self.matrix[i][j] = min(rep, ins, delete)

        

        return self.matrix

    #repair the name of the card from the cards list
    def repair(self, brokenCard, allCards):
        assert(brokenCard != None and allCards != None) #Precondition
        for i in range (allCards):
            repairMatrix = self.LD(allCards[i])
            procentLen = 100 / len(brokenCard.name)
            match = len(brokenCard.name) - repairMatrix[len(brokenCard.name)][len(allCards[i])] * procentLen
            if(match >= 90):
                j = repairMatrix[len(brokenCard.name)][len(allCards[i])]
                x1 = len(brokenCard.name)
                y1 = len(allCards[i])
                while (j is not repairMatrix[0][0]):
                    northwest = repairMatrix[x1-1][y1-1]
                    west = repairMatrix[x1-1][y1]
                    north = repairMatrix[x1][y1-1]
                    if min(northwest, north, west) is northwest:
                        replace(x1, allCards[i][y1])
                        x1 = x1 - 1
                        y1 = y1 - 1
                    elif min(northwest, north, west) is north:
                        insert(x1,  allCards[i][y1])
                        y1 = y1 - 1
                    elif min(northwest, north, west) is west:
                        delete(x1);
                        x1 = x1 - 1
                    j = repairMatrix[x1][y1]



        return self.card

    #inserts the letter c at the index i
    def insert(self, i, c):
        assert(i > 0) #Precondition

        self.card.name = self.card.name[:i - 1] + c + self.card.name[i - 1:]


        assert(self.card.name[i] == c) #Postcondition (Letter c ist an index i)
        pass

    #deletes the letter at the index i
    def delete(self, i):
        assert(i > 0) #Precondition

        self.card.name = self.card.name[0 : i :] + self.card.name[i + 1 : :]

        assert() #Postcondition (Alte Wortlaenge - 1)
        pass

    #replaces the letter at index i with c.
    def replace(self, i, c):
        assert(i > 0) #Precondition (Letter c ist an index i)

        self.card.name = self.card.name[:i].replace(self.card.name[i], c) + line[i:]

        pass


