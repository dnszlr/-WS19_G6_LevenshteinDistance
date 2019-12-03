import os
import unittest
from CardCollector import CardCollector
from Card import Card

class CardCollectorTest(unittest.TestCase):

    def setUp(self):
        self.collector = CardCollector()

    def testReadFile(self):
        
        file = self.collector.readFile("reference")
        print(file.read())

    def testBuildScrambled(self):

        self.collector.buildScrambled("scrambled")
        print("Scrambled card names: ")
        for cardName in self.collector.brokenCards:
            print(cardName.name)

    def testBuildReference(self):

        self.collector.buildReference("reference")
        print("Reference cards: ")
        for cardName in self.collector.referenceNames:
            print(cardName)
            
    def testWriteFile(self):

        repaired = [Card("test", "4", "4", "one", "3")]
        self.collector.repairedCards = repaired
        self.collector.writeFile("test")

if __name__ == '__main__':
    unittest.main()      