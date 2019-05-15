dx = [0,0,1,-1]
dy = [1,-1,0,0]
m = 0
n = 0
result = []
def dfs(x,y,flag,maze):
    flag[x][y] = 1
    if(maze[x][y] == 'T'):
        return True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<m and ny<n and flag[nx][ny] == 0 and(maze[nx][ny] == '0' or maze[nx][ny] == 'T'):
            result.append([nx,ny])
            return dfs(nx,ny,flag,maze)
            flag[nx][ny] = 0
    return False

if __name__ == "__main__":
    m = 3
    n = 3
    maze = [['0', '0', '0'],['*', '*', '0'], ['*', '0', '0']]
    maze[m-1][n-1] = 'T'
    flag = [[0 for i in range(n)] for j in range(m)]
    result = [[0,0]]
    dfs(0,0,flag,maze)
    print(result)

    