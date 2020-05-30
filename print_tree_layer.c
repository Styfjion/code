#include <stdio.h>
#include "securec.h"
#include "hlist.h"
#define MAX 100
typedef struct List List;

typedef struct {
    int childNum;
    int children[MAX];
} Leaf;

typedef struct {
    struct Node node;
    int index;
} Queue;

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
        Queue *unit = LIST_HEAD_ENTRY(list, Queue, node);
        while (unit != NULL) {
            count++;
            unit = LIST_NEXT_ENTRY(unit, list, Queue, node);
        }
    return count;
    }
}

void BFS(Leaf *nodes, List *list) {
    while (ListEmpty(list) == false) {
        int length = QueueSize(list);
        Queue *unit;
        for (int i = 0; i < length; i++) {
            unit = LIST_HEAD_ENTRY(list, Queue, node);
            ListRemoveHead(list);
            int index = unit->index;
            g_path[i] = index;
            for (int j = 0; j < nodes[index].childNum; j++) {
                Queue *item = (Queue *)malloc(sizeof(Queue));
                item->index = nodes[index].children[j];
                ListAddTail(list, &item->node);
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
    Queue *head = (Queue *)malloc(sizeof(Queue));
    head->index = 0;
    ListAddTail(&list, &head->node);
    BFS(nodes, &list);
    PrintPath();
    return 0;
}
