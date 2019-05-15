class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        found = False
        if array:
            row = 0
            column = len(array[0])-1
            while(column>=0 and row<=len(array)-1):
                if (target==array[row][column]):
                    found = True
                    break
                elif target<array[row][column]:
                    column -= 1
                else:
                    row += 1
        return found