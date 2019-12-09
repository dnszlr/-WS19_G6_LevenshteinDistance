from CardCollector import CardCollector
from CardRepair import CardRepair
from multiprocessing import Pool
import time
import sys

startTime = time.time()
if __name__=='__main__':
        collector1 = CardCollector()
        pool = Pool(10)
        collector1.buildScrambled("scrambled")
        collector1.buildReference("reference")
        numbers = range(len(collector1.brokenCards))
        r = pool.map_async(collector1.getRepairedCard, numbers) 
        pool.close()
        pool.join()
        collector1.repairedCards = r.get()
        collector1.writeFile("Arbeitspferd")
        print(time.time() - startTime)




