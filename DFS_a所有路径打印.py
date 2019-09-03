import copy
class DFS:
    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    def __init__(self,beginX,beginY,endX,endY):
        self.count = 0
        self.beginX = beginX
        self.beginY = beginY
        self.endX = endX
        self.endY = endY
        self.result = []
        self.path = []


    def dfs_operation(self,matrix,x,y):
        rows = len(matrix)
        cols = len(matrix[0])
        if x == self.endX and y == self.endY:
            self.count += 1
            self.result.append(copy.deepcopy(self.path))
        if x<0 or x>=rows or y<0 or y>=cols:
            return
        for i in range(4):
            nx = x + self.dir[i][0]
            ny = y + self.dir[i][1]
            if nx>=0 and nx<rows and ny>=0 and ny<cols and matrix[nx][ny]!=1:
                matrix[nx][ny] = 1
                self.path.append([nx,ny])
                self.dfs_operation(matrix,nx,ny)
                matrix[nx][ny] = 0
                self.path.pop()

if __name__ == "__main__":
    matrix = [[0,1,0,0,0,1],[0,0,0,1,0,0],[1,0,1,0,0,1],[1,0,0,1,0,1],[1,1,0,0,0,0]]
    rows = len(matrix)
    columns = len(matrix[0])
    dfs = DFS(0,0,rows-1,columns-1)
    dfs.path.append([0,0])
    matrix[0][0] = 1
    dfs.dfs_operation(matrix,0,0)
    print(dfs.count)
    for unit in dfs.result:
        print(unit) 

        

