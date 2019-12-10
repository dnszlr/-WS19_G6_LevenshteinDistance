class CardRepair(object):
    #description of class

    def __init__(self, card, allCards):
        assert card != None and allCards != None #Precondition
        self.card = card
        self.allCards = allCards

    #create the LD-matrix
    def LD(self, referenceName):

        #Preconditin
        assert(referenceName != None)
        assert(len(self.card.name) >= 1 and  len(referenceName) >= 1)

        x = len(self.card.name)
        y = len(referenceName)
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

        assert(matrix != None) #Postcondition
        return matrix

    #repair the name of the card from the cards list
    def repair(self):
        assert(self.card != None) #Precondition

        for i in range (len(self.allCards)):

            #if(abs(len(self.card.name) - len(self.allCards[i])) < 3):
            if(len(self.card.name) == len(self.allCards[i])):

                repairMatrix = self.LD(self.allCards[i])
                match = (repairMatrix[len(self.card.name)][len(self.allCards[i])] * 100) / len(self.card.name)
                if(match <= 50):
                    j = repairMatrix[len(self.card.name)][len(self.allCards[i])]
                    x1 = len(self.card.name)
                    y1 = len(self.allCards[i])
                    while (j is not repairMatrix[0][0]):
                        northwest = repairMatrix[x1-1][y1-1]
                        west = repairMatrix[x1-1][y1]
                        north = repairMatrix[x1][y1-1]
                        if min(northwest, north, west) is west:
                            self.card.delete(x1-1)
                            x1 = x1 - 1
                        elif min(northwest, north, west) is north:
                            self.card.insert(x1, self.allCards[i][y1-1])
                            y1 = y1 - 1
                        elif min(northwest, north, west) is northwest:
                            self.card.replace(x1-1, self.allCards[i][y1-1])
                            x1 = x1 - 1
                            y1 = y1 - 1
                        j = repairMatrix[x1][y1]
                        
                        #print(self.card.name + ": " + str(match) + ":" + self.allCards[i])
                    if(self.card.name != self.allCards[i]):
                        print(self.card.name + "|" + self.allCards[i])
                    return self.card
        print("failed")
        assert(self.card != None) #Postcondition

        return self.card