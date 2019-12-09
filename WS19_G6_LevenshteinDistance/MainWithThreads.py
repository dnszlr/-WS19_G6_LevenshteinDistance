from CardCollector import CardCollector
from CardRepair import CardRepair
from multiprocessing import Pool

if __name__=='__main__':
        pool = Pool(10)
        
        collector1 = CardCollector()
        collector1.buildScrambled("scrambled")
        collector1.buildReference("reference")
        numbers = range(len(collector1.brokenCards))
        r = pool.map_async(collector1.getRepairedCard, numbers)
        pool.close()
        pool.join()
        print(collector1.repairedCards)
        #collector1.writeFile("RepairedCards1")




