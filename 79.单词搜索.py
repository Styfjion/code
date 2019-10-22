#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (38.22%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    22.4K
# Total Submissions: 57.2K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        marked = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def match(marked,x,y,index):
            if board[x][y] == word[index]:
                if index == len(word)-1:
                    return True
                for i in range(4):
                    nx = x + dir[i][0]
                    ny = y + dir[i][1]
                    if nx>=0 and nx<len(board) and ny>=0 and ny<len(board[0]) and not marked[nx][ny]:
                        marked[nx][ny] = True
                        if match(marked,nx,ny,index+1):
                            return True
                        marked[nx][ny] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    marked[i][j] = True
                    if match(marked,i,j,0):
                        return True
                    marked[i][j] = False
        return False
                    

        

# @lc code=end

