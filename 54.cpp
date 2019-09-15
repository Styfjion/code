struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
class Solution {
    public:
        int index = 0;
        TreeNode* KthNode(TreeNode* pRoot, int k)
        {
            if(pRoot == nullptr)
                return NULL;
            TreeNode* left = KthNode(pRoot->left,k);
            if(left!=nullptr)
                return left;
            this->index ++;
            if(this->index == k)
                return pRoot;
            TreeNode* right = KthNode(pRoot->right,k);
            if(right!=nullptr)
                return right;
            return NULL;
        } 
};