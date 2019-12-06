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

        repaired = [Card("test7", "42342", "4", "one", "3")]
        self.collector.brokenCards = [Card("Ganutles? of Chaos", "42342", "4", "one", "3"), Card("B?i?er F?ud", "42342", "4", "one", "3"), Card("Ccylop?an?T?mb", "42342", "4", "one", "3"),Card("Elven ?rot?es?", "42342", "4", "one", "3"), Card("uBried R?i?", "42342", "4", "one", "3"), Card("Reflectin? Mirror", "42342", "4", "one", "3")]
        self.collector.referenceNames = ["Slagstorm","Elven Fortress","Drawn Together","Raging Ravine","Buried Ruin","Reflecting Mirror" ,"Elven Rite"]
        self.collector.getRepairedCardsList()
        #self.collector.repairedCards = repaired
        print(self.collector.repairedCards[0].name)
        print(len(self.collector.repairedCards))
        self.collector.writeFile("test2")


if __name__ == '__main__':
    unittest.main()      