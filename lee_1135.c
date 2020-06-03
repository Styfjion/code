#include <stdlib.h>
#include <stdio.h>
int g_num;

typedef struct {
    int x;
    int y;
    int weight;
} Node;

int NodeCmp (const void * p1, const void * p2) {
    Node *node1 = (Node *)p1;
    Node *node2 = (Node *)p2;
    return (node1->weight - node2->weight);
}

int FindRoot (int root, int *pre) {
    int son,tmp;
    son = root;
    while (root != pre[root]) {
        root  = pre[root];
    }
    while (son != root) {
        tmp = pre[son];
        pre[son] = root;
        son = tmp;
    }
    return root;
}

int minimumCost(int N, int **connections, int connectionsSize, int* connectionsColSize){
    g_num = N;
    if (connectionsSize == 0 || connectionsSize < N - 1 ) {
        return -1;
    } 
    int pre[N];
    Node nodes[connectionsSize];
    for (int i = 1; i <= N; i++) {
        pre[i] = i;
    }
    memset(nodes, 0, sizeof(nodes));
    for (int i = 0; i < connectionsSize; i++) {
        nodes[i].x = connections[i][0];
        nodes[i].y = connections[i][1];
        nodes[i].weight = connections[i][2];
    }
    qsort(nodes, connectionsSize, sizeof(Node), NodeCmp);
    int cumSum = 0;
    for (int i = 0; i < connectionsSize; i++) {
        if (g_num == 1) {
            break;
        }
        int root1 = FindRoot(nodes[i].x, pre);
        int root2 = FindRoot(nodes[i].y, pre);
        if (root1 != root2) {
            pre[root1] = root2;
            g_num--;                                       //条件也可改为判断边数是否达到N-1
            cumSum += nodes[i].weight;
        }
    }
    if(g_num > 1) {
        return -1;
    }
    return cumSum;
}

int main(int argc, char const *argv[])
{
    int m[3][3] ={{1,2,5},{1,3,6},{2,3,1}};
    int **a = malloc(3 * sizeof(int));
    for (int i = 0; i < 3; i++) {
        a[i] = malloc(3 * sizeof(int));
        memcpy(a[i], m[i], 3 * sizeof(int));
    }
    int connectionsColSize = 3;
    printf("%d", minimumCost(3, a, 3, &connectionsColSize));
    return 0;
}
