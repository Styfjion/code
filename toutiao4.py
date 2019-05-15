maze = [[0 for i in range(101)] for i in range(101)]
vis = [[0 for i in range(101)] for i in range(101)]借助指示矩阵
dir = [[0,1],[0,-1],[1,0],[-1,0]]
path = []
result = []
rows = 0
cols = 0
count = 0

def dfs(x,y):
    global count
    if x == rows-1 and y == cols-1:
        count += 1
        result.append([unit for unit in path])
        #print(path)直接打印出来
        return
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx >=0 and nx < rows and ny >=0 and ny < cols and not maze[nx][ny] and not vis[nx][ny]:
            maze[nx][ny] = 2
            path.append([nx,ny])
            dfs(nx,ny)
            maze[nx][ny] = 0
            path.pop()


if __name__ == "__main__":
    path = [[0,0]]
    '''
    inputList = list(map(int,input().split()))
    rows = inputList[0]
    cols = inputList[1]
    for i in range(rows):
        line = list(map(int,input().split()))
        for j,v in enumerate(line):
            maze[i][j] = v
    '''
    rows =5
    cols = 6
    lines = [[0,1,0,0,0,1],[0,0,0,1,0,0],[1,0,1,0,0,1],[1,0,0,1,0,1],[1,1,0,0,0,0]]
    for i in range(rows):
        for j in range(cols):
            maze[i][j] = lines[i][j]
    dfs(0,0)
    print(count)
    for unit in result:
        print(unit)
    
