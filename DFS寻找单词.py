dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y,maze,trace,word):
    if maze[x][y] == word[0] and len(word) == 1:
        return True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and ny>=0 and nx < len(maze) and ny < len(maze[0]) and maze[nx][ny] == word[1] and trace[nx][ny] == 0:
            trace[nx][ny] = 1
            ch = word.pop(0)
            if dfs(nx,ny,maze,trace,word[:]):
                return True
            trace[nx][ny] = 0
            word.insert(0,ch)
    return False


if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    word = list(input().strip())
    maze = []
    for _ in range(n):
        maze.append(list(input().strip()))
    token = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == word[0]:
                trace = [[0 for _ in range(m)] for _ in range(n)]
                if dfs(i,j,maze,trace,word[:]):
                    print("YES")
                    token = 1
                    break
    if token == 0:
        print("NO")


