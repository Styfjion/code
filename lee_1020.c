#include <stdlib.h>
#include <stdio.h>
#define MAX 100

//DFS回溯超时
/*
int g_min = -1;
int g_length = 0;
int g_Path[MAX*MAX];
int g_trace[MAX][MAX] = {0};
int R, C;
int direction[2][4] ={{1,-1,0,0},{0,0,1,-1}};

int FindMin(int *array, int length) {
    int min = array[0];
    for (int i = 1; i < length; i++)
    {
        min = array[i] > min ? min : array[i];
    }
    return min;
}

void DFS(int A[][5], int x, int y) {
    if (x == R - 1 && y == C - 1) {
        int minNum = FindMin(g_Path, g_length);
        if (g_min == -1) {
            g_min = minNum;
        } else {
            g_min = g_min < minNum ? minNum : g_min;
        }
    }
    for (int i = 0; i < 4; i++) {
        int nx = x + direction[0][i];
        int ny = y + direction[1][i];
        if (nx < R && ny < C && nx >-1 && ny >-1 && g_trace[nx][ny] == 0) {
            g_Path[g_length++] = A[nx][ny];
            g_trace[nx][ny] = 1;
            DFS(A, nx, ny);
            g_trace[nx][ny] = 0;
            g_length--;
        }
    }
}

int maximumMinimumPath(int A[][5], int ASize, int* AColSize){
    R = ASize;
    C = *AColSize;
    g_Path[g_length++] = A[0][0];
    g_trace[0][0] = 1;
    DFS(A, 0, 0);
    return g_min;
}

int main(int argc, char const *argv[])
{
    int A[][5] = {{3,4,6,3,4},{0,2,1,1,7},{8,8,3,2,7},{3,2,4,9,8},{4,1,2,0,0},{4,6,5,4,3}};
    int ASzie = 6;
    int AColSize = 5;
    printf("%d",maximumMinimumPath(A, ASzie, &AColSize));
    return 0;
}
*/
#define min(a,b) (a) < (b) ? (a) : (b)
int direction[2][4] = {{1,-1,0,0},{0,0,1,-1}};
typedef struct {
    int x;
    int y;
    int value;
} Node;

int NodeCmp (const void *p1, const void *p2)
{
    return (((Node *)p2)->value - ((Node*)p1)->value);
}

int FindRoot (int root, int *parent) {
    int son,tmp;
    son = root;
    while (root != parent[root]) {
        root = parent[root];
    }
    while (son != root) {
        tmp = parent[son];
        parent[son] = root;
        son = tmp;
    }
    return root;
}

void Union(int x, int y, int *parent) 
{
    int rootX, rootY;
    rootX = FindRoot(x, parent);
    rootY = FindRoot(y, parent);
    if (rootX == rootY) {
        return;
    } else if (rootX < rootY) {
        parent[rootX] = rootY;
    } else {
        parent[rootY] = rootX;
    }
}
int maximumMinimumPath(int** A, int ASize, int* AColSize){
    int matrixSize = ASize * (*AColSize);
    int trace[matrixSize];
    int parent[matrixSize];
    Node nodeArray[matrixSize];
    memset(trace, 0, sizeof(trace));
    memset(parent, 0, sizeof(parent));
    memset(nodeArray,0,sizeof(nodeArray));
    int count = 0;
    for (int i = 0; i < ASize; i++) {
        for (int j = 0; j < (*AColSize); j++) {
            parent[count] = i * (*AColSize) + j;
            nodeArray[count].x = i;
            nodeArray[count].y = j;
            nodeArray[count].value = A[i][j];
            count++;
        }
    }
    qsort(nodeArray, matrixSize, sizeof(Node), NodeCmp);
    count = 0;
    int ans = min(A[0][0], A[ASize - 1][*AColSize - 1]);
    while (FindRoot(0, parent) != FindRoot(matrixSize - 1, parent)) {
        int x = nodeArray[count].x;
        int y = nodeArray[count].y;
        int index = x * (*AColSize) + y;
        trace[index] = 1;
        ans = min(ans, nodeArray[count].value);
        for (int i = 0; i < 4; i++)
        {
            int nx, ny;
            nx = x + direction[0][i];
            ny = y + direction[1][i];
            int indexNew = nx * (*AColSize) + ny;
            if (nx < ASize && nx > -1 && ny < (*AColSize) && ny > -1 && trace[indexNew] == 1) {
                Union(index, indexNew, parent);
            }
        }
        count++;
    }
    return ans;
}



int main(int argc, char const *argv[])
{
    int A[][5] = {{3,4,6,3,4},{0,2,1,1,7},{8,8,3,2,7},{3,2,4,9,8},{4,1,2,0,0},{4,6,5,4,3}};
    int ASzie = 6;
    int AColSize = 5;
    printf("%d",maximumMinimumPath(A, ASzie, &AColSize));
    return 0;
}

