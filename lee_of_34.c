#include <stdio.h>
#include <string.h>
#define MAX 10000

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode TreeNode;

int g_result[MAX];
int g_pathNum;

void AddPath(TreeNode *treeNode, int level, int **ans, int** returnColumnSizes) {
    (*returnColumnSizes)[g_pathNum] = level;
    ans[g_pathNum] = malloc(level * sizeof(int));
    memcpy(ans[g_pathNum], g_result, level * sizeof(int));
    g_pathNum++;
}

void DFS(TreeNode *treeNode, int level, int **ans, int sum, int target, int** returnColumnSizes) {
    if (treeNode->left == NULL && treeNode->right == NULL) {
        if (sum == target) {
            AddPath(treeNode, level, ans, returnColumnSizes);
        }
        return;
    }
    if (treeNode->left != NULL) {
        g_result[level] = treeNode->left->val;
        DFS(treeNode->left, level+1, ans, sum + g_result[level], target, returnColumnSizes);
    }
    if (treeNode->right != NULL) {
        g_result[level] = treeNode->right->val;
        DFS(treeNode->right, level+1, ans, sum + g_result[level], target, returnColumnSizes);
    }
}

int** pathSum(struct TreeNode* root, int sum, int* returnSize, int** returnColumnSizes){
    g_pathNum = 0;
    memset(g_result, 0, MAX * sizeof(int));
    if (root == NULL) {
        *returnSize = g_pathNum;
        return NULL;
    }
    int **ans = malloc(MAX * sizeof(int *));
    g_result[0] = root->val;
    int currSum = root->val;
    DFS(root, 1, ans, currSum, sum, returnColumnSizes);
    *returnSize = g_pathNum;
    return ans;
}