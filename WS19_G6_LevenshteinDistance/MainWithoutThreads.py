from CardCollector import CardCollector
from CardRepair import CardRepair
import time


startTime = time.time()
if __name__=='__main__':
        collector1 = CardCollector()

        collector1.buildScrambled("scrambled")
        collector1.buildReference("reference")
      
        collector1.getRepairedCardsList()

        #print(collector1.repairedCards[0].name)
        #print(len(collector1.repairedCards))
        
        collector1.writeFile("ArbeitspferdOhneThreads")
        print(time.time() - startTime)




