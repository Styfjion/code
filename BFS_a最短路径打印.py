class Node:
    def __init__(self,x,y,pre,step):
        self.x = x
        self.y = y
        self.pre = pre
        self.step = step

class BFS:
    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    def bfs_operation(self,matrix,beginX,beginY,endX,endY):
        rows = len(matrix)
        cols = len(matrix[0])
        matrix[beginX][beginY] = '#'
        queue = []
        begin = Node(beginX,beginY,None,0)
        queue.append(begin)
        while queue:
            top = queue.pop(0)
            if top.x == endX and top.y == endY:
                return top
            for i in range(4):
                nx = top.x + self.dir[i][0]
                ny = top.y + self.dir[i][1]
                if nx>=0 and nx<rows and ny>=0 and ny<cols and matrix[nx][ny] != '#':
                    matrix[nx][ny] = '#'
                    queue.append(Node(nx,ny,top,top.step+1))
        return
    
    def print_path(self,beginX,beginY,node):
        if node.x == beginX and node.y == beginY:
            print(node.x,end=' ')
            print(node.y)
            return
        self.print_path(beginX,beginY,node.pre)
        print(node.x,end = ' ')
        print(node.y)

if __name__ == "__main__":
    N = int(input())
    matrix = []
    beginX = -1
    beginY = -1
    endX = -1
    endY = -1
    for i in range(N):
        rows = list(input())
        for j in range(len(rows)):
            if rows[j] == 'S':
                beginX = i
                beginY = j
            if rows[j] == 'E':
                endX = i
                endY = j
        matrix.append(rows)
    bfs = BFS()
    end = bfs.bfs_operation(matrix,beginX,beginY,endX,endY)
    if not end:
        bfs.print_path(beginX,beginY,end)
    else:
        print("No path")
