class Solution:
    def printMatrix(self, matrix):
        return matrix and list(matrix.pop(0))+self.printMatrix(list(zip(*matrix))[::-1])

class Solution2:
    def PrintMatrixClockwisely(self,matrix):
        if not matrix:
            return
        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        newSequence = []
        while columns > start*2 and rows > start*2:
            self.PrintMatrixInCircle(matrix,start,newSequence)
            start += 1
        return newSequence
    def PrintMatrixInCircle(self,matrix,start,result):
        rows = len(matrix)
        columns = len(matrix[0])
        endX = columns - 1 - start
        endY = rows - 1 - start
        for i in range(start,endX+1):
            result.append(matrix[start][i])
        if endY > start:
            for i in range(start+1,endY+1):
                result.append(matrix[i][endX])
            if endX > start:
                for i in range(endX-1,start-1,-1):
                    result.append(matrix[endY][i])
                if endY-1 > start:
                    for i in range(endY-1,start,-1):
                        result.append(matrix[i][start])
        return result
