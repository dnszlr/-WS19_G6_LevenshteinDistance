from CardCollector import CardCollector
from CardRepair import CardRepair
from multiprocessing import Pool
from threading import Thread
import time
import sys

startTime = time.time()
if __name__=='__main__':
        collector1 = CardCollector()
        
        t1 = Thread(target = collector1.buildScrambled, args = ("scrambled",))
        t1.start()
        t1.join()        
        t2 = Thread(target = collector1.buildReference, args = ("reference",))
        t2.start()
        t2.join()
        #collector1.buildScrambled("scrambled")
        #collector1.buildReference("reference")
        numbers = range(len(collector1.brokenCards))
        pool = Pool(10)
        r = pool.map_async(collector1.getRepairedCard, numbers) 
        pool.close()
        pool.join()
        collector1.repairedCards = r.get()
        collector1.writeFile("Arbeitspferd")
        print(time.time() - startTime)




