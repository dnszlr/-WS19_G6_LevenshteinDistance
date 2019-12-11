import unittest
from Card import *

#unittest for the class Card
class Test_CardTest(unittest.TestCase):
    
    def setUp(self):
       
        self.card = Card("Tester", 1,2,3,4)

    #Calling the insert function from Card
    def testInsert(self):

        assert(self.card is not None)
        oldLen = len(self.card.name)
        self.card.insert(2, "B")
        assert(oldLen < len(self.card.name))
        assert(self.card.name[2] is "B")
    
    #Calling the delete function from Card
    def testDelete(self):

        assert(self.card is not None)
        oldLen = len(self.card.name)
        self.card.delete(2)
        assert(oldLen > len(self.card.name))
    
    #Calling the replace function from Card
    def testReplace(self):
        
        assert(self.card is not None)
        self.card.replace(2, "B")
        assert(self.card.name[2] is "B")

if __name__ == '__main__':
    unittest.main()
