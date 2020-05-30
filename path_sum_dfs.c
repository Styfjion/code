/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2019-2019. All rights reserved.
 * Description: 树形网络
 * Note: 缺省代码仅供参考，可自行决定使用、修改或删除
 */

#include <stdio.h>
#include "securec.h"
#define min(a,b) (((a) < (b)) ? (a) : (b))

#define MAXN 100

int gPathNum = 0;
int gPaths[MAXN][MAXN] = {0};
int gPathLength[MAXN] = {0};
int gResult[MAXN] = {0};

typedef struct _Node {
    int val;
    int child[MAXN];
    int childNum;
} Node;

int arrcmp(int a, int b) {
    int minLen = min(gPathLength[a], gPathLength[b]);
    for (int i = 0; i < minLen; i++) {
        if (gPaths[a][i] > gPaths[b][i]) {
            return 1;
        }
        
        if (gPaths[a][i] < gPaths[b][i]) {
            return -1;
        }
    }
    
    return gPathLength[a] - gPathLength[b];
}

void swap(int a, int b)
{
    int tmp[MAXN] = {0};
    memcpy_s(tmp, MAXN * sizeof(int), gPaths[a], MAXN * sizeof(int));
    memcpy_s(gPaths[a], MAXN * sizeof(int), gPaths[b], MAXN * sizeof(int));
    memcpy_s(gPaths[b], MAXN * sizeof(int), tmp, MAXN * sizeof(int));
    
    int temp = gPathLength[a];
    gPathLength[a] = gPathLength[b];
    gPathLength[b] = temp;
}

int partition(int* arr[], int startIndex, int endIndex)
{
    int left = startIndex;
    int right = endIndex;

    while (left != right) {
        while (left < right && arrcmp(right, startIndex) > 0) {
            right--;
        }

        while (left < right && arrcmp(left, startIndex) <= 0) {
            left++;
        }

        if (left < right) {
            swap(left, right);
        }
    }

    swap(left, startIndex);
    return left;
}

void quickSort(int* arr[], int startIndex, int endIndex)
{
    // 递归结束条件，startIndex大等于endIndex
    if (startIndex >= endIndex) {
        return;
    }
    // 得到基准元素位置
    int pivotIndex = partition(arr, startIndex, endIndex);
    quickSort(arr, startIndex, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, endIndex);
}

void addPath(int level, Node* nodes, int index)
{
    /* 如果不是叶子节点，则返回 */
    if (nodes[index].childNum != 0) {
        return;
    }
    
    if (memcpy_s(gPaths[gPathNum], MAXN * sizeof(int), gResult, level * sizeof(int)) != EOK) {
        return;
    }
    gPathLength[gPathNum] = level;
    gPathNum++;
}

void printPath(int index, int length)
{
    for (int i = 0; i < length - 1; i++) {
        printf("%d ", gPaths[index][i]);
    }
    printf("%d\n", gPaths[index][length - 1]);
}

void print()
{
    for (int j = gPathNum - 1; j >= 0; j--) {
        printPath(j, gPathLength[j]);
    }
}

void dfs(int index, int sum, Node* nodes, int target, int level)
{
    if (sum == target) {
        addPath(level, nodes, index);
        return;
    }
    
    if (sum > target) {
        return;
    }
    
    if (nodes[index].childNum == 0) {
        return;
    }
    
    for (int i = 0; i < nodes[index].childNum; i++) {
        int val = nodes[nodes[index].child[i]].val;
        gResult[level] = val;
        dfs( nodes[index].child[i], sum + val, nodes, target, level + 1);
    }
}

/* 请按需拆分或重组函数，避免过高的圈复杂度 */ 
int main(void)
{ 
    /* 全局变量初始化 */
    gPathNum = 0;
    memset(gPaths, 0, MAXN * MAXN * sizeof(int));
    memset(gPathLength, 0, MAXN * sizeof(int));
    memset(gResult, 0, MAXN * sizeof(int));
    
    /* 输入 */
    int n, m, s;
    if (scanf_s("%d %d %d", &n, &m, &s) != 3) {
        return -1;
    }
    
    Node* nodes = (Node*)malloc(sizeof(Node) * MAXN);
    if (nodes == NULL) {
        return -1;
    }
    memset(nodes, 0, sizeof(Node) * MAXN);

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
            nodes[parent].child[j] = child;
        }
    }
    
    int sum = nodes[0].val;
    gResult[0] = nodes[0].val;
    int level = 0;
    dfs(0, sum, nodes, s, level + 1);
    quickSort(gPaths, 0, gPathNum - 1);
    print();
    return 0;
}