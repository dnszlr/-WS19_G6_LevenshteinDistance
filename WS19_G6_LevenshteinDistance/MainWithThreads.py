from CardCollector import CardCollector
from CardRepair import CardRepair
from multiprocessing import Pool
from multiprocessing import Process
import time
import sys

startTime = time.time()
if __name__=='__main__':
        collector1 = CardCollector()
        
        #process1 = Process(target = collector1.buildScrambled, args=("scrambled",))
        #process1.start()
        #process1.join()
        collector1.buildScrambled("scrambled")
        collector1.buildReference("reference")
        numbers = range(len(collector1.brokenCards))
        pool = Pool(10)
        r = pool.map_async(collector1.getRepairedCard, numbers) 
        pool.close()
        pool.join()
        collector1.repairedCards = r.get()
        collector1.writeFile("Arbeitspferd")
        print(time.time() - startTime)




