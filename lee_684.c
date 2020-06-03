
#include <stdlib.h>

int Findroot (int root, int *pre) 
{
    int son, tmp;
    son = root;
    while (root != pre[root]) {
        root = pre[root];
    }
    while (son != root) {
        tmp = pre[son];
        pre[son] = root;
        son = tmp;
    }
    return root;
}

int* findRedundantConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize){
    if (edgesSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    int pre[edgesSize + 1];
    for (int i = 1; i <= edgesSize; i++) {
        pre[i] = i;
    }
    int point = 0;
    for (int i = 0; i < edgesSize; i++) {
        int  root1 = Findroot(edges[i][0], pre);
        int  root2 = Findroot(edges[i][1], pre);
        if (root1 == root2)
        {
            point = i;
        } else {
            pre[root1] = root2;
        }
    }
    *returnSize = 2;
    return edges[point];
}