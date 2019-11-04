maze = [[0 for i in range(101)] for i in range(101)]
dir = [[0,1],[0,-1],[1,0],[-1,0]]
class Node:
    x = -1
    y = -1
    prex = -1
    prey = -1

def bfs(rows,cols,path):
    queue = []
    path[0][0].x = path[0][0].y = 0
    maze[0][0] = 1
    queue.append(path[0][0])
    while queue:
        top = queue.pop(0)
        if top.x == rows-1 and top.y == cols-1:
            return
        for i in range(4):
            nx = top.x + dir[i][0]
            ny = top.y + dir[i][1]
            if nx >=0 and nx < rows and ny >=0 and ny < cols and not maze[nx][ny]:
                path[nx][ny].x = nx
                path[nx][ny].y = ny
                path[nx][ny].prex = top.x
                path[nx][ny].prey = top.y
                maze[nx][ny] = 1
                queue.append(path[nx][ny])

def printPath(x,y):
    if not x and not y:
        print(path[0][0].x, end = ' ')
        print(path[0][0].y)
        return
    px = path[x][y].prex
    py = path[x][y].prey
    printPath(px,py)
    print(path[x][y].x, end = ' ')
    print(path[x][y].y)

if __name__ == "__main__":
    rows = 5
    cols = 6
    lines = [[0,1,0,0,0,1],[0,0,0,1,0,0],[1,0,1,0,0,1],[1,0,0,1,0,1],[1,1,0,0,0,0]]
    for i in range(rows):
        for j in range(cols):
            maze[i][j] = lines[i][j]
    path = [[Node() for i in range(cols)] for i in range(rows)]
    bfs(rows,cols,path)
    printPath(rows-1,cols-1)


