
class Matrix(object):
    """description of class"""

    def __init__(self, stringS, stringT):

        self.matrix = [[0 for x in range(len(stringS) + 1)] for y in range(len(stringT) + 1)]

        for i in range(0, len(self.matrix)):
            matrix[i][0] = i
            for j in range(0, len(matrix[i])):
                matrix[0][j] = j


