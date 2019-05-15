matrix = []
def change(matrix):
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    rows = len(matrix)
    cols = len(matrix[0])
    num = 0
    while True:
        token = 2+num
        for i in range(rows):
            if not token in matrix[i]:
                continue
            index = matrix[i].index(token)
            for j in range(index,cols):
                if matrix[i][j] == token:
                    flag = False
                    for k in range(4):
                        nx = i + dir[k][0]
                        ny = j + dir[k][1]
                        if nx >=0 and nx < rows and ny >=0 and ny < cols and matrix[nx][ny] == 1:
                            matrix[nx][ny] = token+1
                            flag = True
                    if flag:
                        matrix[i][j] = token+1
        arraymatrix = []
        for unit in matrix:
            arraymatrix += unit
        num += 1
        if max(arraymatrix) <= 2:
            return -1
        if not 1 in arraymatrix:
            break
    return num

if __name__ == "__main__":
    count = 0
    while True:
        line = input()
        if not line:
            break
        matrix.append(list(map(int,line.split())))
    count = change(matrix)     
    print(count)
