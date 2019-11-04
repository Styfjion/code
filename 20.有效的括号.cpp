/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 *
 * https://leetcode-cn.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (39.87%)
 * Likes:    1139
 * Dislikes: 0
 * Total Accepted:    143.1K
 * Total Submissions: 358.8K
 * Testcase Example:  '"()"'
 *
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
 * 
 * 有效字符串需满足：
 * 
 * 
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 * 
 * 
 * 注意空字符串可被认为是有效字符串。
 * 
 * 示例 1:
 * 
 * 输入: "()"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: "()[]{}"
 * 输出: true
 * 
 * 
 * 示例 3:
 * 
 * 输入: "(]"
 * 输出: false
 * 
 * 
 * 示例 4:
 * 
 * 输入: "([)]"
 * 输出: false
 * 
 * 
 * 示例 5:
 * 
 * 输入: "{[]}"
 * 输出: true
 * 
 */

// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> dict;
        dict[')'] = '(';
        dict[']'] = '[';
        dict['}'] = '{';
        stack<char> st;
        for (char ch : s)
        {
            if (dict.find(ch) != dict.end())
            {
                if (st.empty())
                {
                    return false;
                }
                if (dict[ch] != st.top())
                {
                    return false;
                }
                else
                {
                    st.pop();
                }
            }
            else
            {
                st.push(ch);
            }
        }
        return st.empty();
    }
};
// @lc code=end

