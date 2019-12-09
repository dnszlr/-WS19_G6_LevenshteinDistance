import unittest
from Card import *
from CardRepair import CardRepair

class Test_CardRepairTest(unittest.TestCase):

    def setUp(self):
       
        self.card1 = Card("Johiar??o th eGhitu Avatar", 2,4,5,6)
        self.card2 = Card("Inufsed?Arrows", 2,4,5,6)
        self.card3 = Card("iiiiiiindustry", 2,4,5,6)
        self.card4 = Card("hallooffrfo", 2,4,5,6)
        self.referenceNames1 = ["Jhoira of the Ghitu Avatar", "Scorching Missile" , "Infused Arrows"]
        self.cardRepair1 = CardRepair(self.card1, self.referenceNames1)
        self.cardRepair2 = CardRepair(self.card2, self.referenceNames1)


    def testLD(self):
        
        assert(self.cardRepair1.LD(self.referenceNames1[1]) is not None)
        assert(self.card1 is not None)
       # self.fail("Not implemented")
         
    def testInsert(self):
        pass
        assert(self.card1 is not None)
        self.cardRepair1.insert(2, "B")
        print("This is testInsert: " + self.cardRepair1.card.name)

    def testDelete(self):
        pass
        assert(self.card1 is not None)
        self.cardRepair1.delete(2)
        print("This is testDelete: " + self.cardRepair1.card.name)

    def testReplace(self):
        pass
        
        assert(self.card1 is not None)
        self.cardRepair1.replace(2, "B")
        print("This is testReplace: " + self.cardRepair1.card.name)
    
    
    def testRepair(self):
        print('broken card: ' + self.card1.name)
        print('broken card: ' + self.card2.name)
        self.cardRepair1.repair()
        self.cardRepair2.repair()
        print('repaired card: ' + self.card1.name)
        print('repaired card: ' + self.card2.name)
   

if __name__ == '__main__':
    unittest.main()
