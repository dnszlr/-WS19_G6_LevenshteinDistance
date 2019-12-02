class CardRepair(object):
    #description of class

    def __init__(self, card, allCards):
        assert card != None && allCards != None #Precondition
        self.card = card
        self.allCards = allCards
        self.matrix = [[]]

    #create the LD-matrix
    def LD(self, referenceCard):
        assert len(self.card.name) >= 1 &&  len(referenceCard.name) >= 1 #Precondition
        return self.matrix

    #repair the name of the card from the cards list
    def repair(self, brokenCard, allCards):
        assert(brokenCard != None && allCards != None) #Precondition
        return self.card

    #inserts the letter c at the index i
    def insert(self, i, c):
        assert(i > 0) #Precondition

        assert() #Postcondition (Letter c ist an index i)
        pass

    #deletes the letter at the index i
    def delete(self, i):
        assert(i > 0) #Precondition

        assert() #Postcondition (Alte Wortlaenge - 1)
        pass

    #replaces the letter at index i with c.
    def replace(self, i, c):
        assert(i > 0) #Precondition (Letter c ist an index i)

        pass


