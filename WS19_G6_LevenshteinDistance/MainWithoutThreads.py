from CardCollector import CardCollector
from CardRepair import CardRepair
import time


startTime = time.time()
if __name__=='__main__':
        collector1 = CardCollector()            #creating a new cardCollector called collector1

        collector1.buildScrambled("scrambled")  #reading the scrambled cards
        collector1.buildReference("reference")  #reading the reference cards 
      
        collector1.getRepairedCardsList()       #repairing the card and getting them

        #print(collector1.repairedCards[0].name)
        #print(len(collector1.repairedCards))
        
        collector1.writeFile("ArbeitspferdOhneThreads") #write them in the file with "Path"
        print(time.time() - startTime)                  #printing the time for this work in seconds




