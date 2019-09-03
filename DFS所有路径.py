class DFS:
    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    def __init__(self, rows, columns,endx,endy):
        self.maze = [[0 for i in range(columns)] for i in range(rows)]
        self.path = []
        self.result = []
        self.count = 0
        self.endx = endx
        self.endy = endy
        self.rows = rows
        self.columns = columns
    
    def dfs_operation(self,x,y):
        if x == self.endx and y == self.endy:
            self.count += 1
            self.result.append([unit for unit in self.path])
        if x<0 or x>=self.rows or y<0 or y>=self.columns:
            return 
        for i in range(4):
            nx = x + self.dir[i][0]
            ny = y + self.dir[i][1]
            if nx>=0 and nx<self.rows and ny>=0 and ny<self.columns and not self.maze[nx][ny]:
                self.maze[nx][ny] = 2
                self.path.append([nx,ny])
                self.dfs_operation(nx,ny)
                self.maze[nx][ny] = 0
                self.path.pop()

if __name__ == "__main__":
    lines = [[0,1,0,0,0,1],[0,0,0,1,0,0],[1,0,1,0,0,1],[1,0,0,1,0,1],[1,1,0,0,0,0]]
    rows = len(lines)
    columns = len(lines[0])
    dfs = DFS(rows,columns,rows-1,columns-1)
    for i in range(rows):
        for j in range(columns):
            dfs.maze[i][j] = lines[i][j]
    dfs.path.append([0,0])
    dfs.maze[0][0] = 2
    dfs.dfs_operation(0,0)
    print(dfs.count)
    for unit in dfs.result:
        print(unit)

"""
2
[[0, 0], [1, 0], [1, 1], [1, 2], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 5]]
[[0, 0], [1, 0], [1, 1], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [4, 4], [4, 5]]

"""
        