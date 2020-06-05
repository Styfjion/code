#include <stdio.h>
#include <stdlib.h>
#include "securec.h"
#define min(a, b) (a) < (b) ? (a) : (b)
#define MAX 100

typedef struct {
    int val;
    int childNum;
    int children[MAX];
} Node;

int g_paths[MAX][MAX + 1] = {0};
int g_result[MAX] = {0};
int g_pathNum = 0;

void AddPath(Node *node, int level)
{
    if (node->childNum != 0) {
        return;
    }
    memcpy_s(g_paths[g_pathNum], MAX * sizeof(int), g_result, level * sizeof(int));
    g_paths[g_pathNum][MAX] = level;
    g_pathNum++;
}

void DFS(Node *tree, int index, int level, int sum, int target)
{
    if (target == sum) {
        AddPath(&tree[index], level);
        return;
    }
    if (sum > target) {
        return;
    }
    if (tree[index].childNum == 0) {
        return;
    }
    for (int i = 0; i < tree[index].childNum; i++) {
        int newIndex = tree[index].children[i];
        g_result[level] = tree[newIndex].val;
        DFS(tree, newIndex, level + 1, sum + tree[newIndex].val, target);
    }
}

void PrintNode()
{
    for (int i = 0; i < g_pathNum; i++) {
        int len = g_paths[i][MAX];
        for (int j = 0; j < len - 1; j++) {
            printf("%d ", g_paths[i][j]);
        }
        printf("%d\n", g_paths[i][len - 1]);
    }
}

int NodeCmp(const void *p1, const void *p2)
{
    int *ch1, *ch2;
    ch1 = (int *)p1;
    ch2 = (int *)p2;
    int length = min(ch1[MAX], ch2[MAX]);
    for (int i = 0; i < length; i++) {
        if (ch1[i] != ch2[i]) {
            return ch2[i] - ch1[i];
        }
    }
    return ch2[MAX] - ch1[MAX];
}

/* 请按需拆分或重组函数，避免过高的圈复杂度 */
int main(void)
{
    int n, m, s;
    if (scanf_s("%d %d %d", &n, &m, &s) != 3) {
        return -1;
    }
    Node tree[n];
    memset(tree, 0, sizeof(tree));
    int i;
    int w;
    for (i = 0; i < n; i++) {
        if (scanf_s("%d", &w) != 1) {
            return -1;
        }
        // TODO: 处理权重
        tree[i].val = w;
    }

    int parent, child;
    int childCnt;
    int j;
    for (i = 0; i < m; i++) {
        if (scanf_s("%d %d", &parent, &childCnt) != 2) {
            return -1;
        }
        tree[parent].childNum = childCnt;
        for (j = 0; j < childCnt; j++) {
            if (scanf_s("%d", &child) != 1) {
                return -1;
            }
            // TODO: 处理父子关系
            tree[parent].children[j] = child;
        }
    }

    int sum = tree[0].val;
    g_result[0] = tree[0].val;
    DFS(tree, 0, 1, sum, s);
    qsort(g_paths, g_pathNum, (MAX + 1) * sizeof(int), NodeCmp);
    PrintNode();
    // TODO: 输出
    return 0;
}
