import os
import unittest
from CardCollector import CardCollector
from Card import Card

class CardCollectorTest(unittest.TestCase):

    def setUp(self):
        self.collector = CardCollector()

    def testRead(self):
        
        file = self.collector.readFile("reference")
        x = file.readline
        print(x)

    def testBuildScrambled(self):
        pass

    def testBuildReference(self):
        pass

    def testWriteFile(self):

        repaired = [Card("test", "2", "3", "one", "3")]
        self.collector.repairedCards = repaired
        self.collector.writeFile("test.txt")

if __name__ == '__main__':
    unittest.main()
       
      