# -*- coding:utf-8 -*-
class Solution:

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold<0 or rows<1 or cols<1:
            return 0
        visited = [False for i in range(rows*cols)]
        count = self.movingCountCore(threshold,rows,0,cols,0,visited)
        return count
    
    def movingCountCore(self,threshold,rows,row,cols,col,visited):
        count  = 0
        if row<0 or row>=rows or col<0 or col>cols:
            return count
        if self.checkEntering(threshold,row,col) and not visited[row*cols+col]:
            visited[row*cols+col] = True
            count = 1 + self.movingCountCore(threshold,rows,row+1,cols,col,visited)+\
            self.movingCountCore(threshold,rows,row-1,cols,col,visited)+\
            self.movingCountCore(threshold,rows,row,cols,col-1,visited)+\
            self.movingCountCore(threshold,rows,row,cols,col+1,visited)
        return count

    def checkEntering(self,threshold,row,col):
        if threshold >= self.getDigtSum(row) + self.getDigtSum(col):
            return True
        else:
            return False
    
    def getDigtSum(self,number):
        sum = 0
        while number>0:
            sum += number%10
            number = int(number/10)
        return sum

if __name__ == "__main__":
    solution = Solution()
    print(solution.movingCount(5,10,10))
            
    

    

            

    
