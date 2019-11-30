class CardRepair(object):
    #description of class

    def __init__(self, card, allCards):
        assert card != None && allCards != None
        self.card = card
        self.allCards = allCards
        self.matrix = [[]]

    #create the LD-matrix
    def LD(self, referenceCard):
        assert len(self.card.name) >= 1 &&  len(referenceCard.name) >= 1
        return self.matrix

    #repair the name of the card from the cards list
    def repair(self, brokenCard, allCards):
        return self.card

    #inserts the letter c at the index i
    def insert(self, i, c):
        pass

    #deletes the letter at the index i
    def delete(self, i):
        pass

    #replaces the letter at index i with c.
    def replace(self, i, c):
        pass


