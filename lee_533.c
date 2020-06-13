#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int row, column, count;

int RowIsSame(char *a, char *b) 
{
    return strncmp(a, b, column);
}

void CalculateNumber(char** picture, int *rowB, int *colB, int N) 
{
    int stack[row];
    int stackLength;
    for (int j = 0; j < column; j++) {
        stackLength = 0;
        for (int i = 0; i < row; i++) {
            if (rowB[i] == N && colB[j] == N && picture[i][j] == 'B') {
                if (stackLength == 0) {
                    stack[stackLength++] = i;
                } else if (RowIsSame(picture[stack[stackLength-1]], picture[i]) == 0) {
                    stack[stackLength++] = i;
                }
            }
        }
        if (stackLength == N) {
            count += stackLength;
        }
    }
}

int findBlackPixel(char** picture, int pictureSize, int* pictureColSize, int N)
{
    row = pictureSize;
    column = *pictureColSize;
    count = 0;
    int rowB[row];
    int colB[column];
    memset(rowB, 0, sizeof(rowB));
    memset(colB, 0, sizeof(colB));
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (picture[i][j] == 'B') {
                rowB[i]++;
                colB[j]++;
            }
        }
    }
    CalculateNumber(picture, rowB, colB, N);
    return count;
}
