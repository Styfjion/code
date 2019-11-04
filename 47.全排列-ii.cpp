/*
 * @lc app=leetcode.cn id=47 lang=cpp
 *
 * [47] 全排列 II
 *
 * https://leetcode-cn.com/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (52.95%)
 * Likes:    172
 * Dislikes: 0
 * Total Accepted:    25.7K
 * Total Submissions: 46.9K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个可包含重复数字的序列，返回所有不重复的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,1,2]
 * 输出:
 * [
 * ⁠ [1,1,2],
 * ⁠ [1,2,1],
 * ⁠ [2,1,1]
 * ]
 * 
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.empty())
            return res;
        if(nums.size() == 1)
        {
            res.push_back(nums);
            return res;
        }
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++)
        {
            if(i>0 && nums[i] == nums[i-1]) continue;
            vector<int> temp;
            if(i>0)
                temp.insert(temp.end(),nums.begin(),nums.begin()+i);
            if(i<nums.size()-1)
                temp.insert(temp.end(),nums.begin()+i+1,nums.end());
            vector<vector<int>> subList;
            subList = permuteUnique(temp);
            for(auto unit:subList)
            {
                unit.push_back(nums[i]);
                res.push_back(unit);
            }
        }
        return res;       
    }
};
// @lc code=end

