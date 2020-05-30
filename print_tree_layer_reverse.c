#include <stdio.h>
#include "hlist.h"
#define MAX 100
typedef struct List List;
typedef struct Node Node;

typedef struct {
    int childNum;
    int index;
    int children[MAX];
    Node node;
} Leaf;


int g_paths[MAX][MAX + 1] = {0};
int g_path[MAX] = {0};
int g_pathNum = 0;

void PrintPath() {
    printf("\0");
    for(int i = 0; i < g_pathNum; i++) {
        int len = g_paths[i][MAX];
        for (int j = 0; j < len - 1; j++) {
            printf("%d ", g_paths[i][j]);
        }
        printf("%d\n", g_paths[i][len - 1 ]);
    }
}

int QueueSize(List *list) {
    if (ListEmpty(list)) {
        return 0;
    } else {
        int count = 0;
        Leaf *unit = LIST_HEAD_ENTRY(list, Leaf, node);
        while (unit != NULL) {
            count++;
            unit = LIST_NEXT_ENTRY(unit, list, Leaf, node);
        }
    return count;
    }
}

void BFS(Leaf *nodes, List *list) {
    while (ListEmpty(list) == false) {
        int length = QueueSize(list);
        Leaf *unit;
        for (int i = 0; i < length; i++) {
            unit = LIST_HEAD_ENTRY(list, Leaf, node);
            ListRemoveHead(list);
            int index = unit->index;
            if (g_pathNum % 2 == 0) {
                g_path[i] = index;
            }
            else {
                g_path[length - 1 - i] = index;
            }
            for (int j = 0; j < nodes[index].childNum; j++) {
                int childIndex = nodes[index].children[j];
                ListAddTail(list, &nodes[childIndex].node);
            }
        }
        memcpy_s(g_paths[g_pathNum], MAX * sizeof(int), g_path, length * sizeof(int));
        g_paths[g_pathNum][MAX] = length;
        g_pathNum++;
    }
}

int main(int argc, char const *argv[])
{
    int n, m;
    if (scanf_s("%d %d", &n, &m) != 2) {
        return -1;
    }
    Leaf *nodes = (Leaf *)malloc(n *sizeof(Leaf));
    memset(nodes, 0, n*sizeof(Leaf));
    for (int i = 0; i < n; i++) {
        nodes[i].index = i;
    }

    int parent, child;
    int childCnt;
    for (int i = 0; i < m; i++) {
        if (scanf_s("%d %d", &parent, &childCnt) != 2) {
            return -1;
        }
        nodes[parent].childNum = childCnt;
        for (int j = 0; j < childCnt; j++) {
            if (scanf_s("%d", &child) != 1) {
                return -1;
            }
            nodes[parent].children[j] = child;
        }
    }
    List list;
    ListInit(&list);
    ListAddTail(&list, &nodes[0].node);
    BFS(nodes, &list);
    PrintPath();
    return 0;
}

/*
输入：
20 9 
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
