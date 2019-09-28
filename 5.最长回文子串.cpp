/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (26.07%)
 * Likes:    1299
 * Dislikes: 0
 * Total Accepted:    112.9K
 * Total Submissions: 415.3K
 * Testcase Example:  '"babad"'
 *
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 * 
 * 示例 1：
 * 
 * 输入: "babad"
 * 输出: "bab"
 * 注意: "aba" 也是一个有效答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入: "cbbd"
 * 输出: "bb"
 * 
 * 
 */
class Solution {
public:
    string longestPalindrome(string s) {
        vector<vector<bool>> dp(s.length(),vector<bool>(s.length(),false));
        for(int i=0;i<s.length();i++)
            dp[i][i] = true;
        int len = s.length();
        int result[] = {0,0};
        for (int i=len-2;i>=0;i--)
            for(int j=i+1;j<len;j++)
            {
                if(j == i+1)
                    dp[i][j] = s[i]==s[j];
                else
                    dp[i][j] == dp[i+1][j-1] && (s[i]==s[j]);
                if(dp[i][j] && (result[1] < j-i))
                {
                    result[0] = i;
                    result[1] = j-i;
                }
            }
        return s.substr(result[0],result[1]+1);
    }
};

