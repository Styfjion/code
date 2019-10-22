/*
 * @lc app=leetcode.cn id=102 lang=cpp
 *
 * [102] 二叉树的层次遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (57.46%)
 * Likes:    294
 * Dislikes: 0
 * Total Accepted:    51.4K
 * Total Submissions: 86.8K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
 * 
 * 例如:
 * 给定二叉树: [3,9,20,null,null,15,7],
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 返回其层次遍历结果：
 * 
 * [
 * ⁠ [3],
 * ⁠ [9,20],
 * ⁠ [15,7]
 * ]
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root == nullptr) return res;
        deque<TreeNode*> queue;
        queue.push_back(root);
        while(!queue.empty())
        {
            vector<int> temp;
            int length = queue.size();
            for(int i=0;i<length;i++)
            {
                TreeNode *top = queue.front();
                temp.push_back(top->val);
                queue.pop_front();
                if(top->left!=nullptr)
                    queue.push_back(top->left);
                if(top->right!=nullptr)
                    queue.push_back(top->right);
            }
            res.push_back(temp);
        }
        return res;
    }
};
// @lc code=end

