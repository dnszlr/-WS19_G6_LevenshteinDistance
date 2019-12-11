import unittest

class Test_CardTest(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

             
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
