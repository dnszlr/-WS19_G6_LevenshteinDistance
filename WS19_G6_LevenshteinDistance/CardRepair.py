class CardRepair(object):
    #description of class

    def __init__(self, card, allCards):
        assert card != None && allCards != None #Precondition
        self.card = card
        self.allCards = allCards
        self.matrix = [[]]

    #create the LD-matrix
    def LD(self, referenceCard):
        assert len(self.card.name) >= 1 &&  len(referenceCard.name) >= 1
        x = len(self.card.name)
        y = len(referenceCard.name)
        self.matrix[0][0] = 0
        for i in range(0, x):
            self.matrix[i][0] = i
        for j in range (0, y):
            self.matrix[0][j] = j
                           
        self.matrix = [[x]y]
        for j in range(1, y):
            for i in range(1, x):
                c = 1
                if (self.card.name[i] is referenceCard.name[j]) : 
                    c = 0
                rep = self.matrix[i-1][j-1] + c
                ins = self.matrix[i][j-1] + 1
                delete = self.matrix[i-1][j] + 1
                self.matrix[i][j] = min(rep, ins, delete)

        

        return self.matrix

    #repair the name of the card from the cards list
    def repair(self, brokenCard, allCards):
        assert(brokenCard != None && allCards != None) #Precondition
        return self.card

    #inserts the letter c at the index i
    def insert(self, i, c):
        assert(i > 0) #Precondition

        assert(splitted[self.card[i]] == c) #Postcondition
        pass

    #deletes the letter at the index i
    def delete(self, i):
        assert(i > 0) #Precondition

        assert() #Postcondition (Alte Wortlaenge - 1)
        pass

    #replaces the letter at index i with c.
    def replace(self, i, c):
        assert(i > 0) #Precondition

        assert(splitted[self.card[i]] == c) #Postcondition
        pass


