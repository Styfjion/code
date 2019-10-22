/*
 * @lc app=leetcode.cn id=79 lang=cpp
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (38.22%)
 * Likes:    224
 * Dislikes: 0
 * Total Accepted:    22.4K
 * Total Submissions: 57.2K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
 * 
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 * 
 * 示例:
 * 
 * board =
 * [
 * ⁠ ['A','B','C','E'],
 * ⁠ ['S','F','C','S'],
 * ⁠ ['A','D','E','E']
 * ]
 * 
 * 给定 word = "ABCCED", 返回 true.
 * 给定 word = "SEE", 返回 true.
 * 给定 word = "ABCB", 返回 false.
 * 
 */

// @lc code=start
class Solution {
public:
    int dir[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
    bool match(vector<vector<char>> &board,vector<vector<bool>> &marked,string word,int x,int y,int index)
    {
        if(board[x][y] == word[index])
        {
            if(index==word.length()-1) 
                return true;
            for(int i=0;i<4;i++)
            {
                int nx,ny;
                nx = x+dir[i][0];
                ny = y+dir[i][1];
                if(nx>=0 && nx<board.size() && ny>=0 && ny<board[0].size() && !marked[nx][ny])
                {
                    marked[nx][ny] = true;
                    if(match(board,marked,word,nx,ny,index+1)) 
                        return true;
                    marked[nx][ny] = false;
                }
            }
        }
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<bool>> marked(board.size(),vector<bool>(board[0].size(),false));
        for(int i=0;i<board.size();i++)
            for(int j=0;j<board[0].size();j++)
            {
                if(board[i][j] == word[0])
                {
                    marked[i][j] = true;
                    if(match(board,marked,word,i,j,0))
                        return true;
                    marked[i][j] = false;   
                }
            }
        return false;
    }
};
// @lc code=end

