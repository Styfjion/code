#include <stdlib.h>
#include <stdio.h>
#define max(a,b) ((a) > (b) ? (a) : (b))

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode TreeNode;

typedef enum {
    CHOOSE = 0,
    NO_CHOOSE = 1
} Choose;

int * RobRecursion(TreeNode *node) {
    int *res = malloc(2 * sizeof(int));
    if (node == NULL) { 
        res[CHOOSE] = 0;
        res[NO_CHOOSE] = 0;
        return res;
    }
    int *resLeft = RobRecursion(node->left);
    int *resRight = RobRecursion(node->right);
    res[CHOOSE] = node->val + resLeft[NO_CHOOSE] + resRight[NO_CHOOSE];
    res[NO_CHOOSE] = max(resLeft[CHOOSE], resLeft[NO_CHOOSE]) + max(resRight[CHOOSE], resRight[NO_CHOOSE]);
    return res;
}

int rob(struct TreeNode* root)
{
    int *res = RobRecursion(root);
    return max(res[CHOOSE], res[NO_CHOOSE]);
}

int main(int argc, char const *argv[])
{
    TreeNode tree[4] = {{2, tree + 1, tree + 2},
                        {1, NULL, tree + 3},
                        {3, NULL, NULL},
                        {4, NULL, NULL}};
    printf("%d", rob(tree));
    return 0;
}
