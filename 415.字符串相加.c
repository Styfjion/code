/*
 * @lc app=leetcode.cn id=415 lang=c
 *
 * [415] 字符串相加
 *
 * https://leetcode-cn.com/problems/add-strings/description/
 *
 * algorithms
 * Easy (46.46%)
 * Likes:    159
 * Dislikes: 0
 * Total Accepted:    33K
 * Total Submissions: 66.1K
 * Testcase Example:  '"0"\n"0"'
 *
 * 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
 * 
 * 注意：
 * 
 * 
 * num1 和num2 的长度都小于 5100.
 * num1 和num2 都只包含数字 0-9.
 * num1 和num2 都不包含任何前导零。
 * 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
 * 
 * 
 */

// @lc code=start

#define MAX_LEN 5100
char strSum[MAX_LEN+2] = {'\0'};
char * addStrings(char * num1, char * num2) {
    int index1,index2;
    int sumIndex = MAX_LEN;
    int token = 0;
    index1 = strlen(num1)-1;
    index2 = strlen(num2)-1;
    while (index1 >= 0 || index2 >= 0 || token == 1) {
        int sumStr;
        sumStr = (index1 >= 0 ? num1[index1]-'0':0) + (index2 >= 0 ? num2[index2]-'0':0) + token;
        strSum[sumIndex--] = sumStr % 10 + '0';
        token = sumStr / 10;
        index1--;
        index2--;
    }
    return &strSum[++sumIndex];
}


// @lc code=end

