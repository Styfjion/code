class Node:
    def __init__(self):
        self.x = None
        self.y = None
        self.prex = None
        self.prey = None
        self.val = None

class BFS:
    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    def __init__(self,rows,cols,beginX,beginY,endX,endY):
        self.rows = rows
        self.cols = cols
        self.maze = [[Node() for i in range(cols)] for j in range(rows)]
        self.endX = endX
        self.endY = endY
        self.beginX = beginX
        self.beginY = beginY

    def bsf_operation(self):
        beginX = self.beginX
        beginY = self.beginY
        queue = []
        self.maze[beginX][beginY].x = self.maze[beginX][beginY].y = 0
        self.maze[beginX][beginY].val = 2
        queue.append(self.maze[beginX][beginY])
        while queue:
            top = queue.pop(0)
            if top.x == self.endX and top.y == self.endY:
                return
            for i in range(4):
                nx = top.x + self.dir[i][0]
                ny = top.y + self.dir[i][1]
                if nx>=0 and nx<self.rows and ny>=0 and ny<self.cols and not self.maze[nx][ny].val:
                    self.maze[nx][ny].x = nx
                    self.maze[nx][ny].y = ny
                    self.maze[nx][ny].val = 2
                    self.maze[nx][ny].prex = top.x
                    self.maze[nx][ny].prey = top.y 
                    queue.append(self.maze[nx][ny])
    
    def print_path(self,x,y):
        if x == self.beginX and y == self.beginY:
            print(x,end = ' ')
            print(y)
            return 
        prex = self.maze[x][y].prex
        prey = self.maze[x][y].prey
        self.print_path(prex,prey)
        print(x,end =' ')
        print(y)
    



    

        
        




