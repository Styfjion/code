/*
 * @lc app=leetcode.cn id=290 lang=cpp
 *
 * [290] 单词规律
 *
 * https://leetcode-cn.com/problems/word-pattern/description/
 *
 * algorithms
 * Easy (39.81%)
 * Likes:    131
 * Dislikes: 0
 * Total Accepted:    18.3K
 * Total Submissions: 43.5K
 * Testcase Example:  '"abba"\n"dog cat cat dog"'
 *
 * 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
 * 
 * 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
 * 
 * 示例1:
 * 
 * 输入: pattern = "abba", str = "dog cat cat dog"
 * 输出: true
 * 
 * 示例 2:
 * 
 * 输入:pattern = "abba", str = "dog cat cat fish"
 * 输出: false
 * 
 * 示例 3:
 * 
 * 输入: pattern = "aaaa", str = "dog cat cat dog"
 * 输出: false
 * 
 * 示例 4:
 * 
 * 输入: pattern = "abba", str = "dog dog dog dog"
 * 输出: false
 * 
 * 说明:
 * 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
 * 
 */

// @lc code=start

//自己答案
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        int n=pattern.size(),i=0;
        map<char,int> dict1;
        map<string,int> dict2;
        istringstream in(str);
        for(string word;in>>word;i++)
        {
            if(i == n)
                return false;
            if(dict1.find(pattern[i]) == dict1.end())
                dict1[pattern[i]] = dict1.size()+1;
            if(dict2.find(word) == dict2.end())
                dict2[word] = dict2.size()+1;
            if(dict1[pattern[i]] != dict2[word])
                return false;
        }
        return i==n;
    }
};

//高票答案
bool wordPattern(string pattern, string str) {
    map<char, int> p2i;
    map<string, int> w2i;
    istringstream in(str);
    int i = 0, n = pattern.size();
    for (string word; in >> word; ++i) {
        if (i == n || p2i[pattern[i]] != w2i[word])
            return false;
        p2i[pattern[i]] = w2i[word] = i + 1;
    }
    return i == n;
}
// @lc code=end

