import os
import unittest
from CardCollector import CardCollector
from Card import Card

class CardCollectorTest(unittest.TestCase):

    def setUp(self):
        self.collector = CardCollector()

    def testBuildScrambled(self):

        self.collector.buildScrambled("scrambled")
        print("Scrambled card names: ")
        assert(len(self.collector.brokenCards) == 663)
        for cardName in self.collector.brokenCards:
            print(cardName.name)

    def testBuildReference(self):
        
        self.collector.buildReference("reference")
        print("Reference cards: ")
        for reference in self.collector.referenceNames:
            print(reference)
        assert(len(self.collector.referenceNames) == 6757) 

    def testWriteFile(self):

        self.collector.buildScrambled("scrambled")   
        self.collector.buildReference("reference")
        self.collector.getRepairedCardsList()
        self.collector.repairedCards = repaired
        print(self.collector.repairedCards[0].name)
        print(len(self.collector.repairedCards))
        self.collector.writeFile("test2")


if __name__ == '__main__':
    unittest.main()      