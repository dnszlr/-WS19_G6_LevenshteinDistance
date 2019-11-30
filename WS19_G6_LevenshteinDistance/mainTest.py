
def main():

    matrix = [[0 for x in range(len("stringS") + 1)] for y in range(len("stringT") + 1)]

    for x in range(0, len(matrix)):
        matrix[x][0] = x
        for y in range(0, len(matrix[x])):
            matrix[0][y] = y

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
main()

if __name__== "__main__":

    main()


    
