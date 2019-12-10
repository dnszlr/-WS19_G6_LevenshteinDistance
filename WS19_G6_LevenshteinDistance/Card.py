
class Card(object):

    def __init__(self, name, mana, cmc, type, count):
        #Class Constructor
        self.name = name
        self.mana = mana
        self.cmc = cmc
        self.type = type
        self.count = count

    #inserts the letter c at the index i
    def insert(self, i, c):
        assert(i >= 0) #Precondition
        self.name = self.name[:i] + c + self.name[i:]
        assert(self.name[i] == c) #Postcondition

    #deletes the letter at the index i
    def delete(self, i):
        assert(i >= 0) #Precondition
        lenOld = len(self.name)
        self.name = self.name[0 : i :] + self.name[i + 1 : :]
        assert(len(self.name) < lenOld) #Postcondition 

    #replaces the letter at index i with c.
    def replace(self, i, c):
        assert(i >= 0) #Precondition
        self.name = self.name[:i] + c + self.name[i + 1:]
        assert(self.name[i] == c) #Postcondition