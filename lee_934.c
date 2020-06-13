#define min(a,b) (a) < (b) ? (a) : (b)
#define MAX 100


typedef struct {
    int x;
    int y;
    int pathLen;
} Node;


int direction[2][4] = {{1,-1,0,0},{0,0,1,-1}};
int row, column;

void DFS(int **A, int x, int y)
{
    for (int i = 0; i < 4; i++) {
        int nx, ny;
        nx = x + direction[0][i];
        ny = y + direction[1][i];
        if (nx < row && nx > -1 && ny < column && ny > -1 && A[nx][ny] == 1) {
            A[nx][ny] = 2;
            DFS(A, nx, ny);
        }
    }
}

int BFS(int **A, int x, int y, int trace[row][column]) 
{
    Node queue[row * column];
    int queueHead, queueTail;
    queueHead = queueTail = 0;
    Node temp = {x, y, 0};
    queue[queueTail++] = temp;
    while (queueHead < queueTail) {
        Node topUnit = queue[queueHead++];
        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = topUnit.x + direction[0][i];
            ny = topUnit.y + direction[1][i];
            if (nx < row && nx > -1 && ny < column && ny > -1 && trace[nx][ny] == 0) {
                if (A[nx][ny] == 2) {
                    return topUnit.pathLen;
                } else if (A[nx][ny] == 0) {
                    trace[nx][ny] = 1;
                    Node temp2 = {nx, ny, topUnit.pathLen + 1};
                    queue[queueTail++] = temp2;
                }
            }
        }
    }
    return row * column;
}

int shortestBridge(int** A, int ASize, int* AColSize){
    row = ASize;
    column = *AColSize;
    int trace[row][column];
    int token = 1;
    int count = row * column;
    for (int i = 0; i < ASize; i++) 
    {
        for (int j = 0; j < (*AColSize); j++) 
        {
            if (A[i][j] == 1) 
            {
                if (token == 1) 
                {
                    A[i][j] = 2;
                    DFS(A, i, j);
                    token++;
                } else 
                {
                    memset(trace, 0, sizeof(trace));
                    int ret = BFS(A, i, j, trace);
                    count = min(count, ret);
                }
            }
        }
    }
    return count;
}