import unittest
from Card import *
from CardRepair import CardRepair

#unittest for the class CardRepair
class Test_CardRepairTest(unittest.TestCase):

    def setUp(self):
       
        self.card1 = Card("D?i? rCharm", 2,4,5,6)       #Creating card1
        self.card2 = Card("Inufsed?Arrows", 2,4,5,6)    #Creating card2
        self.card3 = Card("iiiiiiindustry", 2,4,5,6)    #Creating card3
        self.card4 = Card("hallooffrfo", 2,4,5,6)       #Creating card4
        self.referenceNames1 = ["Dimir Charm", "Scorching Missile" , "Infused Arrows"]  #Creating reference names
        self.cardRepair1 = CardRepair(self.card1, self.referenceNames1)                 
        self.cardRepair2 = CardRepair(self.card2, self.referenceNames1)


    #Calling the LD function from CardRepair and try it with card1
    def testLD(self):
        
        assert(self.cardRepair1.LD(self.referenceNames1[1]) is not None)
        assert(self.card1 is not None)
    
    #Calling the repair function from CardRepair
    def testRepair(self):
        print('broken card: ' + self.card1.name)
        print('broken card: ' + self.card2.name)
        self.cardRepair1.repair()
        self.cardRepair2.repair()
        print('repaired card: ' + self.card1.name)
        print('repaired card: ' + self.card2.name)
   

if __name__ == '__main__':
    unittest.main()
