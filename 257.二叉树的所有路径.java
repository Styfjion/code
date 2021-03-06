

/*
 * @lc app=leetcode.cn id=257 lang=java
 *
 * [257] 二叉树的所有路径
 *
 * https://leetcode-cn.com/problems/binary-tree-paths/description/
 *
 * algorithms
 * Easy (58.85%)
 * Likes:    146
 * Dislikes: 0
 * Total Accepted:    13.5K
 * Total Submissions: 22.7K
 * Testcase Example:  '[1,2,3,null,5]'
 *
 * 给定一个二叉树，返回所有从根节点到叶子节点的路径。
 * 
 * 说明: 叶子节点是指没有子节点的节点。
 * 
 * 示例:
 * 
 * 输入:
 * 
 * ⁠  1
 * ⁠/   \
 * 2     3
 * ⁠\
 * ⁠ 5
 * 
 * 输出: ["1->2->5", "1->3"]
 * 
 * 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {

    private List<String> paths = new LinkedList<>();
    private void constructPath(TreeNode root, String path){
        if(root!=null)
        {
            path += Integer.toString(root.val);
            if(root.left == null && root.right == null)
                this.paths.add(path);
            else{
                path += "->";
                if (root.left!=null)
                    this.constructPath(root.left, path);
                if (root.right!=null)
                    this.constructPath(root.right, path);
            }
        }
    }

    public List<String> binaryTreePaths(TreeNode root) {
        this.constructPath(root, "");
        return this.paths;
    }
}

