
def main():
    stringS =list( "interestsfdfd")
    stringT = list("industry")
    matrix = [[0 for x in range(len(stringS) + 1)] for y in range(len(stringT) + 1)]

    for x in range(0, len(matrix)):
        matrix[x][0] = x
        for y in range(0, len(matrix[x])):
            matrix[0][y] = y

    for y in range(1, len(stringT)):
        for x in range(1, len(stringS)):
            if(stringS[x-1] is stringT[y-1]):
                 matrix[x][y] = matrix[x-1][y-1]
            else:
                 matrix[x][y] = matrix[x-1][y-1] + 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
main()

if __name__== "__main__":

    main()

    
