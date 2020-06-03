#include <stdio.h>
#include <stdlib.h>
#include "hlist.h"
#define MAX 1000

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode TreeNode;
typedef struct Node Node;
typedef struct List List;

typedef struct {
    TreeNode *treeNode;
    Node node;
} Dequeue;

int DequeueSize(List *list) {
    int count = 0;
    Dequeue *dequeue = LIST_HEAD_ENTRY(list, Dequeue, node);
    while (dequeue != NULL) {
        count++;
        dequeue = LIST_NEXT_ENTRY(dequeue, list, Dequeue, node);
    }
    return count;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes){
    int **ans = malloc(MAX * sizeof(int *));
    int column = 0;
    if (root == NULL) {
        *returnSize = column;
        return ans;
    }
    List list;
    ListInit(&list);
    Dequeue *head = malloc(sizeof(Dequeue));
    head->treeNode = root;
    ListAddTail(&list, &head->node);
    while (ListEmpty(&list) == false) {
        int length = DequeueSize(&list);
        (*returnColumnSizes)[column] = length;
        ans[column] = malloc(length * sizeof(int));
        for (int i = 0; i < length; i++) {
            Dequeue *top = LIST_HEAD_ENTRY(&list, Dequeue, node);
            ListRemoveHead(&list);
            if (column % 2 == 0) {
                ans[column][i] = top->treeNode->val;
            } else {
                ans[column][length - 1 - i] = top->treeNode->val;
            }
            if (top->treeNode->left != NULL) {
                Dequeue *node1 = malloc(sizeof(Dequeue));
                node1->treeNode = top->treeNode->left;
                ListAddTail(&list, &node1->node);
            }
            if (top->treeNode->right != NULL) {
                Dequeue *node2 = malloc(sizeof(Dequeue));
                node2->treeNode = top->treeNode->right;
                ListAddTail(&list, &node2->node);
            }
        }
        column++;        
    }
    *returnSize = column;
    return ans;
}