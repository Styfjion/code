/*
 * @lc app=leetcode.cn id=199 lang=cpp
 *
 * [199] 二叉树的右视图
 *
 * https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
 *
 * algorithms
 * Medium (59.31%)
 * Likes:    82
 * Dislikes: 0
 * Total Accepted:    6.4K
 * Total Submissions: 10.7K
 * Testcase Example:  '[1,2,3,null,5,null,4]'
 *
 * 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
 * 
 * 示例:
 * 
 * 输入: [1,2,3,null,5,null,4]
 * 输出: [1, 3, 4]
 * 解释:
 * 
 * ⁠  1            <---
 * ⁠/   \
 * 2     3         <---
 * ⁠\     \
 * ⁠ 5     4       <---
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        if(root == nullptr)
            return ret;
        deque<TreeNode*> queue(1,root); 
        while (!queue.empty())
        {
            int length = queue.size();
            int val = 0;
            bool token = false;
            for(int i=0;i<length;i++)
            {
                TreeNode* top;
                token = true;
                top = queue.front();
                queue.pop_front();
                val = top->val;
                if(top->left!=nullptr)
                    queue.push_back(top->left);
                if(top->right!=nullptr)
                    queue.push_back(top->right);
            }
            if(token)
                ret.push_back(val);
        }
        return ret;
    }
};
// @lc code=end

