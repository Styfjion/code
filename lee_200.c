/*DFS深度优先遍历*/
int direction[2][4] = {{1,-1,0,0},{0,0,1,-1}};
int R, C;

void DFS(int x, int y, char** grid)
{
    for (int i = 0; i < 4; i++) {
        int nx, ny;
        nx = x + direction[0][i];
        ny = y + direction[1][i];
        if (nx > -1 && nx < R && ny > -1 && ny < C && grid[nx][ny] == '1') {
            grid[nx][ny] = '0';
            DFS(nx, ny, grid);
        }
    }
}

int numIsland_1(char** grid, int gridSize, int* gridColSize){
    if(gridSize == 0) {
        return 0;
    }
    R = gridSize;
    C = *gridColSize;
    int count = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (grid[i][j] == '1') {
                grid[i][j] = '0';
                DFS(i, j, grid);
                count++;
            }
        }
    }
    return count;
}

/*并查集*/
int g_num;
int FindRoot (int root, int *pre)
{
    int son, tmp;
    son = root;
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
    if(gridSize == 0) {
        return 0;
    }
    int matrixSize = gridSize * (*gridColSize);
    int pre[matrixSize], rank[matrixSize];
    memset(pre, -1, sizeof(pre));
    memset(rank, 0, sizeof(rank));
    R = gridSize;
    C = *gridColSize;
    g_num = 0;
    int count = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (grid[i][j] == '1') {
                pre[i * C + j] = i * C + j;
                rank[i * C + j] = 1;
                g_num++;
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