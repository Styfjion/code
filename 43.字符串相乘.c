/*
 * @lc app=leetcode.cn id=43 lang=c
 *
 * [43] 字符串相乘
 *
 * https://leetcode-cn.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (39.80%)
 * Likes:    218
 * Dislikes: 0
 * Total Accepted:    29.9K
 * Total Submissions: 73.5K
 * Testcase Example:  '"2"\n"3"'
 *
 * 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
 * 
 * 示例 1:
 * 
 * 输入: num1 = "2", num2 = "3"
 * 输出: "6"
 * 
 * 示例 2:
 * 
 * 输入: num1 = "123", num2 = "456"
 * 输出: "56088"
 * 
 * 说明：
 * 
 * 
 * num1 和 num2 的长度小于110。
 * num1 和 num2 只包含数字 0-9。
 * num1 和 num2 均不以零开头，除非是数字 0 本身。
 * 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
 * 
 * 
 */

// @lc code=start

//优化竖式的方法
char * multiply(char * num1, char * num2){
    int len1=strlen(num1),len2=strlen(num2);
    if(strcmp(num1,"0")==0||strcmp(num2,"0")==0)
        return "0";
    char *ans=(char *)malloc(sizeof(char)*(len1+len2+1));//两位数的乘积，结果为3位数或者4位数
    memset(ans,'0',sizeof(char)*(len1+len2+1));
    ans[len1+len2]='\0';

    for (int i=len1-1;i>=0;i--) {
        int n1=num1[i]-'0';
        for (int j=len2-1;j>=0;j--) {
            int n2=num2[j]-'0';
            int sum=(ans[i+j+1]-'0'+n1*n2);
            ans[i+j+1]=sum%10+'0';
            ans[i+j]+=sum/10;
        }
    }
    if (ans[0]=='0')
        ans++;
    return ans;
}


// @lc code=end

