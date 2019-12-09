from CardCollector import CardCollector
from CardRepair import CardRepair
from multiprocessing import Pool

repairedCardsCopy = []


if __name__=='__main__':
        collector1 = CardCollector()
        pool = Pool(10)
        collector1.buildScrambled("scrambled")
        collector1.buildReference("reference")
        numbers = range(len(collector1.brokenCards))
        r = pool.map_async(collector1.getRepairedCard, numbers)
               
        pool.close()
        pool.join()
        repairedCardsCopy.append(r.get(timeout=4500))
        collector1.repairedCards.append(r.get(timeout=4500))
        
        collector1.writeFile("RepairedCards2")




