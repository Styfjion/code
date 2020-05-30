#include <stdio.h>
#include <securec.h>
#define MAX 100

typedef struct {
    int childNum;
    int children[MAX];
} Node;

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

void DFS (Node *nodes, int level, int index) {
    if(nodes[index].childNum == 0) {
        memcpy_s(g_paths[g_pathNum], sizeof(int) * MAX, g_path, sizeof(int) * level);
        g_paths[g_pathNum][MAX] = level;
        g_pathNum++;
        return;
    }
    for (int i = 0; i < nodes[index].childNum; i++) {
        g_path[level] = nodes[index].children[i];
        DFS(nodes, level + 1, nodes[index].children[i]);
    }
}

int main(int argc, char const *argv[])
{
    int n, m;
    if (scanf_s("%d %d", &n, &m) != 2) {
        return -1;
    }
    Node *nodes = (Node *)malloc(n *sizeof(Node));
    memset(nodes, 0, n*sizeof(Node));

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
    g_path[0] = 0;
    DFS(nodes, 1, 0);
    PrintPath();
    return 0;
}
