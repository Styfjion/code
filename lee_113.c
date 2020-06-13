#include <stdio.h>
#include <stdlib.h>
#define MAX 1024

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode TreeNode;

int g_path[MAX];
int g_pathLength[MAX];
int g_pathNum;

void AddPath (TreeNode *node, int level, int **result) {
    if (node->left || node->right) {
        return;
    }
    result[g_pathNum] = malloc(level * sizeof(int));
    memcpy(result[g_pathNum], g_path, level * sizeof(int));
    g_pathLength[g_pathNum] = level;
    g_pathNum++;
}

void DFS (TreeNode *node, int curSum, int sum, int level, int **result)
{
    if (sum == curSum) {
        AddPath(node, level, result);
    }
    if (!node->right && !node->left) {
        return;
    }
    if (node->left) {
        int val = node->left->val;
        g_path[level] = val;
        DFS(node->left, curSum + val, sum, level + 1, result);
    }
    if (node->right) {
        int val = node->right->val;
        g_path[level] = val;
        DFS(node->right, curSum + val, sum, level + 1, result);
    }
}

int** pathSum(struct TreeNode* root, int sum, int* returnSize, int** returnColumnSizes)
{
    if (root == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    g_pathNum = 0;
    memset(g_path, 0, sizeof(g_path));
    memset(g_pathLength, 0, sizeof(g_pathLength));
    g_path[0] = root->val;
    int **result = malloc(MAX * sizeof(int *));
    DFS(root, root->val, sum, 1, result);
    *returnSize = g_pathNum;
    (*returnColumnSizes) = malloc(g_pathNum * sizeof(int));
    memcpy(*returnColumnSizes, g_pathLength, g_pathNum * sizeof(int));
    return result;
}