/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 *
 * https://leetcode-cn.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (46.18%)
 * Likes:    123
 * Dislikes: 0
 * Total Accepted:    7.9K
 * Total Submissions: 16.8K
 * Testcase Example:  '10'
 *
 * 编写一个程序，找出第 n 个丑数。
 * 
 * 丑数就是只包含质因数 2, 3, 5 的正整数。
 * 
 * 示例:
 * 
 * 输入: n = 10
 * 输出: 12
 * 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
 * 
 * 说明:  
 * 
 * 
 * 1 是丑数。
 * n 不超过1690。
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
       int p2,p3,p5;
       p2 = p3 = p5 = 0;
       vector<int> res;
       res.push_back(1);
       for(int i=1;i<n;i++)
       {
           int temp[] = {2*res[p2],3*res[p3],5*res[p5]};
           res.push_back(*min_element(temp,temp+3));
           while (res[i]>=res[p2]*2) p2++;
           while (res[i]>=res[p3]*3) p3++;
           while (res[i]>=res[p5]*5) p5++;
       }
       return res[res.size()-1]; 
    }
};
// @lc code=end

