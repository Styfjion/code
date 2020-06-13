#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int direction[2][2] = {{0,1},{1,0}};
int row, column;

bool DFS(int x, int y, char** picture, int flag)
{
    if (x == row || y == column) {
        return true;
    }
    int nx = x + direction[flag][0];
    int ny = y + direction[flag][1];
    if (nx < row && ny < column && picture[nx][ny] == 'B') {
        return false;
    } else {
        return DFS(nx, ny, picture, flag);
    }
}

int findLonelyPixel(char** picture, int pictureSize, int* pictureColSize)
{
    row = pictureSize;
    column = *pictureColSize;
    int visitedR[row], visitedC[column];
    int count = 0;
    memset(visitedR, 0, sizeof(visitedR));
    memset(visitedC, 0, sizeof(visitedC));
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (picture[i][j] == 'B') {
                if (visitedR[i] == 0 && visitedC[j] == 0) {
                    if (DFS(i, j, picture, 0) && DFS(i, j, picture, 1)) {
                    count++;
                    }
                }
                visitedR[i] = 1;
                visitedC[j] = 1;
            }
        }
    }
    return count;
}

int main(int argc, char const *argv[])
{
    char input[][3] = {{'B', 'B', 'B'}, {'B', 'B', 'B'},{'B', 'B', 'B'}};
    int a = 3;
    char **picture = malloc(3 * sizeof(char *));
    for (int i = 0; i < 3; i++) {
        picture[i] = malloc(3);
        memcpy(picture[i], input[i], 3);
    }
    printf("%d", findLonelyPixel(picture, 3, &a));
    return 0;
}

/*
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
 */
