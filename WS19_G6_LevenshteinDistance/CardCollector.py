import os

class CardCollector(object):
    #Description of class
    #Class attributes

    def __init__(self):

        self.brokenCards = []
        self.referenceCards = []
        self.repairedCards = []

    #Reads from the a .txt-File into a list
    #Returns a new list with cards
    def readReference(self, file):
        assert(file != None) #Preconditon

        path = "../WS19_G6_LevenshteinDistance/Files/" + file + ".txt"
        textFile = open(path, r)

        return None

    #Writes the repairedCards into a selected path
    #Parameters:
    #path - create a new file with the given path
    def write(self, file):
        assert(file != None) #Precondition

        return None

    def relPath(self, file):

        filePath = os.path.dirname(__file__)
        relPath = "../WS19_G6_LevenshteinDistance/Files/" + file + ".txt"
        absFilePath = os.path.join(filePath, relPath)
        






