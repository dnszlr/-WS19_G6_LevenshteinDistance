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
        t2 = Thread(target = collector1.buildReference, args = ("reference",))#creating thread with his task 
        t1.start()      #Start thread
        t2.start()
        t1.join()   
        t2.join()
        numbers = range(len(collector1.brokenCards))            #saving the number of broken cards in numbers
        pool = Pool(10)                                         #creating a pool of processes
        r = pool.map_async(collector1.getRepairedCard, numbers) #r inintialise the process
        pool.close()                                            #closing process
        pool.join()                                             #waiting till al processes finished
        collector1.repairedCards = r.get()                      #r.get() starts and put the repaired cards in a List
        collector1.writeFile("repaired")                   
        print(time.time() - startTime)




