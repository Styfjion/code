#include <stdlib.h>
#include <string.h>
#include "securec.h"
#define MAX 5000
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 };

typedef struct TreeNode TreeNode;
 
 
int treeLengthOne;
int treeLengthTwo;


void MiddleTraversing(TreeNode *node, int *treeNode, int index)
{
    if (node == NULL) {
        return;
    }
    MiddleTraversing(node->left, treeNode, index);
    if (index == 1) {
        treeNode[treeLengthOne++] = node->val;
    } else {
        treeNode[treeLengthTwo++] = node->val;
    }
    MiddleTraversing(node->right, treeNode, index);
} 

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize){
    treeLengthOne = treeLengthTwo = 0;
    int treeNodeOne[MAX], treeNodeTwo[MAX];
    MiddleTraversing(root1, treeNodeOne, 1);
    MiddleTraversing(root2, treeNodeTwo, 2);
    *returnSize = treeLengthTwo + treeLengthOne;
    int *res = malloc((*returnSize) * sizeof(int));
    int index1, index2, index;
    index = index1 = index2 = 0;
    while (index1 < treeLengthOne && index2 < treeLengthTwo) {
        if (treeNodeOne[index1] < treeNodeTwo[index2]) {
            res[index++] = treeNodeOne[index1++];
        } else {
            res[index++] = treeNodeTwo[index2++];
        }
    }
    if (index1 < treeLengthOne) {
        memcpy(res + index, treeNodeOne + index1, (treeLengthOne - index1) * sizeof(int));
    }
    if (index2 < treeLengthTwo) {
        memcpy(res + index, treeNodeTwo + index2, (treeLengthTwo - index2) * sizeof(int));
    }
    return res;
}

int main(int argc, char const *argv[])
{
    TreeNode tree1[3] = {{2, tree1 + 1, tree1 + 2}, 
                         {1, NULL, NULL}, 
                         {4, NULL, NULL}};
    TreeNode tree2[3] = {{1, tree2 + 1, tree2 + 2}, 
                         {0, NULL, NULL}, 
                         {3, NULL, NULL}};

    int returnSize, *res;
    res = getAllElements(tree1, tree2, &returnSize);
    printf("%d", returnSize);
    return 0;
}


