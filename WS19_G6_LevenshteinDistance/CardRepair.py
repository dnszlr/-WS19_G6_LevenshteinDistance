class CardRepair(object):

    #class has a card and allCards
    def __init__(self, card, allCards):
        assert card != None and allCards != None #Precondition
        self.card = card
        self.allCards = allCards


    #create the LD-matrix
    def LD(self, referenceName):

        #Preconditin
        assert(referenceName != None)
        assert(len(self.card.name) >= 1 and len(referenceName) >= 1)

        x = len(self.card.name)
        y = len(referenceName)
        matrix = [[0 for i in range(y+1)] for i in range(x+1)]      #filling the matrix with 0 and the length from both cardnames
        
        matrix[0][0] = 0
        for i in range(0, x+1):     #x+1 becasue of the numbers of the length from cardname
            matrix[i][0] = i        #getting the numbers of cardname length and print it into Martix
        for j in range (0, y+1):    #y+1 becasue of the numbers of the length from reference name
            matrix[0][j] = j        #getting the numbers of reference name length and print it into Martix
        
        for j in range(1, y+1):
            for i in range(1, x+1):
                c = 1
                if (self.card.name[i-1] is referenceName[j-1]) :    #if letter is the same which will be copmared c=0
                    c = 0
                rep = matrix[i-1][j-1] + c                          #filling matrix with numbers
                ins = matrix[i][j-1] + 1
                delete = matrix[i-1][j] + 1
                matrix[i][j] = min(rep, ins, delete)

        assert(matrix != None) #Postcondition
        return matrix

    #repair the name of the card from the cards list
    #repair if accordance is over 50 %
    def repair(self):
        assert(self.card != None) #Precondition
        i = 0
        found = False
        while (i < len(self.allCards) and not found):

            if(len(self.card.name) == len(self.allCards[i])):

                repairMatrix = self.LD(self.allCards[i])
                match = (repairMatrix[len(self.card.name)][len(self.allCards[i])] * 100) / len(self.card.name)
                if(match <= 50):
                    j = repairMatrix[len(self.card.name)][len(self.allCards[i])]
                    x1 = len(self.card.name)
                    y1 = len(self.allCards[i])
                    while (j is not repairMatrix[0][0]):        #while we not on [0][0]
                        northwest = repairMatrix[x1-1][y1-1]    
                        west = repairMatrix[x1-1][y1]
                        north = repairMatrix[x1][y1-1]
                        minValue = min(northwest, north, west)
                        if minValue == west:
                            self.card.delete(x1-1)
                            x1 = x1 - 1
                        elif minValue == north:
                            self.card.insert(x1, self.allCards[i][y1-1])
                            y1 = y1 - 1
                        elif minValue == northwest:
                            self.card.replace(x1-1, self.allCards[i][y1-1])
                            x1 = x1 - 1
                            y1 = y1 - 1
                        j = repairMatrix[x1][y1]
                    found = True
            i = i + 1
        assert(self.card != None) #Postcondition
        return self.card