
class Card(object):

    #Name, Mana, CMC, Type, Count Attributes of every Card
    #Class Constructor
    def __init__(self, name, mana, cmc, type, count):
        self.name = name
        self.mana = mana
        self.cmc = cmc
        self.type = type
        self.count = count