# -*- coding:utf-8 -*
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows < 1 or cols < 1:
            return False
        visted = [False for i in range(rows*cols)]
        pathLength = 0
        if len(path) > len(matrix):
            return False
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, row, cols, col, path, pathLength, visted):
                    return True

    def hasPathCore(self, matrix, rows, row, cols, col, path, pathLength, visted):
        if pathLength == len(path):
            return True
        hasPath = False
        if row >= rows or row < 0 or col >= cols or col < 0:
            return hasPath
        if not visted[row*cols+col] and matrix[row*cols+col] == path[pathLength]:
            pathLength += 1
            visted[row*cols+col] = True
            hasPath = (self.hasPathCore(matrix, rows, row-1, cols, col, path, pathLength, visted)
                       or self.hasPathCore(matrix, rows, row+1, cols, col, path, pathLength, visted)
                       or self.hasPathCore(matrix, rows, row, cols, col-1, path, pathLength, visted)
                       or self.hasPathCore(matrix, rows, row, cols, col+1, path, pathLength, visted))
        if not hasPath:
                pathLength -= 1
                visted[row*cols+col] = False
        return hasPath
