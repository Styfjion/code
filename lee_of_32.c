#include <stdlib.h>
#include "hlist.h"
#define MAX 1000
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode TreeNode;
typedef struct List List;

typedef struct Queue
{
    TreeNode *treeNode;
    struct Node node;
} Queue;

int* levelOrder(struct TreeNode* root, int* returnSize){
    if (root == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int *result = malloc(MAX * sizeof(int));
    int count = 0;
    
    result[count++] = root->val;
    List list;
    ListInit(&list);
    Queue *head = malloc(sizeof(Queue));
    head->treeNode = root;
    ListAddTail(&list, &head->node);
    while (!ListEmpty(&list)) {
        Queue *top = LIST_HEAD_ENTRY(&list, Queue, node);
        ListRemoveHead(&list);
        if (top->treeNode->left != NULL) {
            result[count++] = top->treeNode->left->val;
            Queue *left = malloc(sizeof(Queue));
            left->treeNode = top->treeNode->left;
            ListAddTail(&list, &left->node);
        }
        if (top->treeNode->right != NULL) {
            result[count++] = top->treeNode->right->val;
            Queue *right = malloc(sizeof(Queue));
            right ->treeNode = top->treeNode->right;
            ListAddTail(&list, &right->node);
        }
    }
    *returnSize = count;
    return result;
}