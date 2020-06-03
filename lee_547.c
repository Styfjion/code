
/*DFS深度优先搜索*/
#include <stdlib.h>


void DFS(int** M, int MSize, int *visited, int index)
{
    for (int i = 0; i < MSize; i++) {
        if(M[index][i] == 1 && visited[i] == 0) {
            visited[i] = 1;
            DFS(M, MSize, visited, i);
        }
    }
}

int findCircleNum_1(int** M, int MSize, int* MColSize){
    int visited[MSize];
    memset(visited, 0, sizeof(visited));
    int count = 0;
    for (int i = 0; i < MSize; i++) {
        if (visited[i] == 0) {
            DFS(M, MSize, visited, i);
            count++;
        }
    }
    return count;
}



/*BFS广度优先搜索*/

#include "hlist.h"
typedef struct List List;
typedef struct Node Node;

typedef struct {
    int index;
    Node node;
} Queue;

int findCircleNum_2(int** M, int MSize, int* MColSize)
{
    int visited[MSize];
    memset(visited, 0, sizeof(visited));
    List list;
    ListInit(&list);
    int count = 0;
    for (int i = 0; i < MSize; i++) {
        if (visited[i] == 0) {
            Queue *node = malloc(sizeof(Queue));
            node->index = i;
            ListAddTail(&list, &node->node);
            while (!ListEmpty(&list)) {
                node = LIST_HEAD_ENTRY(&list, Queue, node);
                ListRemoveHead(&list);
                visited[node->index] = 1;
                for (int j = 0; j < MSize; j++)
                {
                    Queue *child;
                    if(M[node->index][j] == 1 && visited[j] == 0) {
                        child = malloc(sizeof(Queue));
                        child->index = j;
                        ListAddTail(&list, &child->node);
                    }
                }
            }
            count++;
        }
    }
    return count;
}

/*并查集*/
int g_count;

int FindRoot(int root, int *parent)
{
    int son, tmp;
    son = root;
    while (root != parent[root]) {
        root = parent[root];
    }
    //路径压缩
    while (son != root) {
        tmp = parent[son];
        parent[son] = root;
        son = tmp;
    }
    return root;
}

void Union(int node1, int node2, int *parent)
{
    int root1, root2;
    root1 = FindRoot(node1, parent);
    root2 = FindRoot(node2, parent);
    if (root1 == root2) {
        return;
    }
    parent[root1] = root2;
    g_count--;
}

int findCircleNum(int** M, int MSize, int* MColSize) 
{
    g_count = MSize;
    int parent[MSize];
    for (int i = 0; i < MSize; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < MSize; i++) {
        for (int j = 0; j < i; j++) {
            if (M[i][j] == 1) {
                Union(i,j,parent);
            }
        }
    }
    return g_count;
}


