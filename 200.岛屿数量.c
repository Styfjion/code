/*
 * @lc app=leetcode.cn id=200 lang=c
 *
 * [200] 岛屿数量
 *
 * https://leetcode-cn.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (44.76%)
 * Likes:    249
 * Dislikes: 0
 * Total Accepted:    32.3K
 * Total Submissions: 70.7K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给定一个由 '1'（陆地）和
 * '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
 * 
 * 示例 1:
 * 
 * 输入:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * 输出: 1
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * 输出: 3
 * 
 * 
 */

// @lc code=start
int direction[2][4] = {{1,-1,0,0},{0,0,1,-1}};
int g_num = 0;
int R, C;
int FindRoot (int root, int *pre)
{
    int son, tmp;
    while (root != pre[root]) {
        root = pre[root];
    }
    while (son != root) {
        tmp = pre[son];
        pre[son] = root;
        son = tmp;
    }
    return root;
}
void Union (int x, int y, int *pre, int *rank) {
    int root1 = FindRoot(x, pre);
    int root2 = FindRoot(y, pre);
    if (root1 == root2) {
        return;
    }
    if(rank[root1] > rank[root2]) {
        pre[root2] = root1;
        rank[root1] += rank[root2];
    } else {
        pre[root1] = root2;
        rank[root2] += rank[root1];
    }
    g_num--;
}

void Neighbor(int x, int y, char **grid, int *pre, int *rank)
{
    int index = x * C + y;
    for (int i = 0; i < 4; i++) {
        int nx = x + direction[0][i];
        int ny = y + direction[1][i];
        if(nx > -1 && nx < R && ny > -1 && ny < C && grid[nx][ny] == '1') {
            int indexNew = nx * C + ny;
            Union(index, indexNew, pre, rank);
        }
    }
}

int numIslands(char** grid, int gridSize, int* gridColSize){
    int matrixSize = gridSize * (*gridColSize);
    int pre[matrixSize], rank[matrixSize];
    memset(pre, -1, sizeof(pre));
    memset(rank, 0, sizeof(rank));
    R = gridSize;
    C = *gridColSize;
    int count = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (grid[i][j] == '1') {
                pre[i * C + j] = i * C + j;
                rank[i * C + j] = 1;
            }
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (grid[i][j] == '1') {
                grid[i][j] = '0';
                Neighbor(i, j, grid, pre, rank);
            }
        }
    }
    return g_num;
}


// @lc code=end

