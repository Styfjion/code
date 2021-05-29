#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/* lee 198 */
class Solution {
public:
    int rob(vector<int>& nums)
    {
        vector<int> dp{0,0};
        for(int i = 0; i < nums.size(); i++) {
            int curVal = max(dp[0] + nums[i], dp[1]);
            dp[0] = dp[1];
            dp[1] = curVal;
        }
        return dp[1];
    }
};

/* lee 213 */
class Solution2 {
public:
    int robSingle(vector<int>& nums)
    {
        vector<int> dp{0,0};
        for(int i = 0; i < nums.size(); i++) {
            int curVal = max(dp[0] + nums[i], dp[1]);
            dp[0] = dp[1];
            dp[1] = curVal;
        }
        return dp[1];
    }
    int rob(vector<int> &nums)
    {
        vector<int> sub1, sub2;
        if (nums.size() == 1) {
            return nums[0];
        }        
        sub1.assign(nums.begin(), nums.end() - 1);
        sub2.assign(nums.begin() + 1, nums.end());
        return max(robSingle(sub1), robSingle(sub2));
    }
};

/* lee 337 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution3 {
public:
    vector<int> Traverse(TreeNode *node)
    {
        if (node == nullptr) {
            return {0, 0};
        }
        auto left = Traverse(node->left);
        auto right = Traverse(node->right);
        int choose = node->val + left[1] + right[1];
        int noChoose = max(left[0], left[1]) + max(right[0], right[1]);
        return {choose, noChoose};
    }
    int rob(TreeNode* root) 
    {
        vector<int> rslt = Traverse(root);
        return max(rslt[0], rslt[1]);
    }
};
