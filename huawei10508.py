
def transMatrix(matrix):
        newmatrix = []
        for i in range(len(matrix)):
            newrow = [unit[i] for unit in matrix]
            newrow = newrow[::-1]
            newmatrix.append(newrow)
        return newmatrix

if __name__ == "__main__":
    N = int(input().strip())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().strip().split())))
    M = int(input().strip())
    for i in range(M):
        matrix = transMatrix(matrix)
    for line in matrix:
        for i in range(N):
            if i<N-1:
                print(line[i],end=' ')
            else:
                print(line[i])
                

        