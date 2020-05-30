#include <stdio.h>
#include <stdlib.h>
#include "securec.h"
#define min(a,b) (((a) < (b)) ? (a) : (b))
#define MAX_N 100

typedef struct {
    int val;
    int childNum;
    int children[MAX_N];
} Node;

int gPathNum = 0;
int gPaths[MAX_N][MAX_N+1] = {0};
int gPath[MAX_N] = {0};    //最后一位存储数组长度

int cmp(const void *n1, const void *n2)
{
    int *pathA = (int *) n1;
    int *pathB = (int *) n2;
    int length = min(pathA[MAX_N], pathB[MAX_N]);
    for (int i = 0; i < length; i++) {
        if (pathA[i] != pathB[i]) {
            return pathA[i] -  pathB[i];
        }
    }
    return pathA[MAX_N] - pathB[MAX_N];
}

void AddPath(Node *node, int level) {
    if (node->childNum != 0) {
        return;
    }
    memcpy_s(gPaths[gPathNum], sizeof(int) * MAX_N, gPath,  sizeof(int) * level);
    gPaths[gPathNum][MAX_N] = level;
    gPathNum++;
}

void DFS(Node *nodes, int index, int level, int sum, int target) {
    if (sum == target) {
        AddPath(&nodes[index], level);
        return;
    }
    if (sum > target) {
        return;
    }
    if (nodes[index].childNum == 0) {
        return;
    }
    for (int i = 0; i < nodes[index].childNum; i++) {
        int val = nodes[nodes[index].children[i]].val;
        gPath[level] = val; 
        DFS(nodes, nodes[index].children[i], level+1, sum+val, target);
    }
}


void PrintPath()
{
    for(int i = gPathNum - 1; i > -1; i--) {
        int len = gPaths[i][MAX_N];
        for (int j = 0; j < len - 1 ; j++) {
            printf("%d ", gPaths[i][j]);
        }
        printf("%d\n", gPaths[i][len - 1]);
    }
}

int main(int argc, char const *argv[])
{
    int n, m, s;
    if (scanf_s("%d %d %d", &n, &m, &s) != 3) {
        return -1;
    }

    Node *nodes = (Node *)malloc(n * sizeof(Node));
    memset(nodes, 0, n * sizeof(Node));
    
        int i;
    int w;
    for (i = 0; i < n; i++) {
        if (scanf_s("%d", &w) != 1) {
            return -1;
        }
        nodes[i].val = w;
    }

    int parent, child;
    int childCnt;
    int j;
    for (i = 0; i < m; i++) {
        if (scanf_s("%d %d", &parent, &childCnt) != 2) {
            return -1;
        }
        nodes[parent].childNum = childCnt;
        for (j = 0; j < childCnt; j++) {
            if (scanf_s("%d", &child) != 1) {
                return -1;
            }
            nodes[parent].children[j] = child;
        }
    }
    int sum = nodes[0].val;
    gPath[0] = sum;
    DFS(nodes, 0, 1, sum, s);
    qsort(gPaths, gPathNum - 1, sizeof(int) * (MAX_N + 1), cmp);
    PrintPath();
    return 0;
}

/*
输入：
20 9 24
10 2 4 3 5 10 2 18 9 7 2 2 1 3 12 1 8 6 2 2
00 4 01 02 03 04
02 1 05
04 2 06 07
03 3 11 12 13
06 1 09
07 2 08 10 
16 1 15
13 3 14 16 17
17 2 18 19
*/

