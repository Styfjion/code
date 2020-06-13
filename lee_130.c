#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int direction[2][4] = {{1,-1,0,0},{0,0,-1,1}};
int row, column;

typedef struct {
    int x;
    int y;
} Node;

bool IsBound(int x, int y)
{
    if(x == 0 || x == row - 1)
    {
        return true;
    } else if (y == 0 || y == column - 1) {
        return true;
    } else {
        return false;
    }
}

void BFS (int x, int y, char **board, int boardSize, int *boardColSize) 
{
    bool visited[row][column];
    memset(visited, 0, sizeof(visited));
    visited[x][y] = true;
    Node queue[(*boardColSize) * boardSize];
    Node path[(*boardColSize) * boardSize];
    int queueHead, queueTail, pathLength;
    queueHead = queueTail = pathLength = 0;
    queue[queueTail].x = x;
    queue[queueTail].y = y;
    queueTail++;
    path[pathLength].x = x;
    path[pathLength].y = y;
    pathLength++;
    while (queueHead < queueTail) {
        Node topUnit = queue[queueHead++];
        if (IsBound(topUnit.x, topUnit.y)) {
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nx,ny;
            nx = topUnit.x + direction[0][i];
            ny = topUnit.y + direction[1][i];
            if (nx < row && nx > -1 && ny < column && ny > -1 && !visited[nx][ny] && board[nx][ny] == 'O') {
                visited[nx][ny] = true;
                queue[queueTail].x = nx;
                queue[queueTail].y = ny;
                queueTail++;
                path[pathLength].x = nx;
                path[pathLength].y = ny;
                pathLength++;
            }
         }
    }
    int tx, ty;
    for (int i = 0; i < pathLength; i++) {
        tx = path[i].x;
        ty = path[i].y;
        board[tx][ty] = 'X';
    }
    return;
}


void solve(char** board, int boardSize, int* boardColSize)
{
    if (boardSize == 0) {
        return;
    }
    row = boardSize;
    column = *boardColSize;
    bool visited[row][column];
    
    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < *boardColSize; j++) {
            if (!visited[i][j] && board[i][j] == 'O') {
                BFS(i, j, board, boardSize, boardColSize);
            }
        }
    }
}

