import os
import unittest
from CardCollector import CardCollector
from Card import Card

class CardCollectorTest(unittest.TestCase):

    def setUp(self):
        self.collector = CardCollector()

    def testRead(self):
        
        file = self.collector.readFile("reference")
        print(file.read())

    def testBuildScrambled(self):
        pass

    def testBuildReference(self):
        pass

    def testWriteFile(self):

        repaired = [Card("test", "4", "4", "one", "3")]
        self.collector.repairedCards = repaired
        self.collector.writeFile("test")

if __name__ == '__main__':
    unittest.main()
       
      