import unittest
from Card import *
from CardRepair import CardRepair

class Test_CardRepairTest(unittest.TestCase):

    def setUp(self):
       
        self.card1 = Card("industry", 2,4,5,6)
        self.card2 = Card("haoo", 2,4,5,6)
        self.card3 = Card("interests", 2,4,5,6)
        self.card4 = Card("hallooffrfo", 2,4,5,6)
        self.list1 = [self.card2, self.card3, self.card4]
        self.cardRepair1 = CardRepair(self.card1, self.list1)


    def testLD(self):
        
        assert(self.cardRepair1.LD(self.list1[1]) is not None)
        assert(self.card1 is not None)
        for i in range(len(self.cardRepair1.matrix)):
            for j in range(len(self.cardRepair1.matrix[i])):
                print(self.cardRepair1.matrix[i][j], end=' ')
            print()
       # self.fail("Not implemented")

    def testInsert(self):

        assert(self.card1 is not None)
        self.cardRepair1.insert(2, "B")
        print("This is testInsert: " + self.cardRepair1.card.name)

    def testDelete(self):

        assert(self.card1 is not None)
        self.cardRepair1.delete(2)
        print("This is testDelete: " + self.cardRepair1.card.name)

    def testReplace(self):

        
        assert(self.card1 is not None)
        self.cardRepair1.replace(2, "B")
        print("This is testReplace: " + self.cardRepair1.card.name)

if __name__ == '__main__':
    unittest.main()
    
