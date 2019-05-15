public class LongestCommonSubstring
{
    public int longestCommonSubstring(String A, String B) {
        // write your code here
        if (A == null || B == null) {
            return 0;
        }
        int n = A.length();
        int m = B.length();
        if (n == 0 || m == 0) {
            return 0;
        }
        int[][] dp = new int[n + 1][m + 1];
        int maxLen = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (A.charAt(i) == B.charAt(j)) {
                    if(i==0||j==0)
                        dp[i][j] = 1;
                    else
                        dp[i][j] = dp[i - 1][j - 1] + 1;
                    maxLen = Math.max(maxLen, dp[i][j]);
                }
            }
        }
        return maxLen;
    }
    public static void main(String[] args) {
        LongestCommonSubstring LCS = new LongestCommonSubstring();
        String A = "abcdfrtgggg", B = "sxtsbfrtggcdc";
        int result;
        result = LCS.longestCommonSubstring(A,B);
        System.out.println(result);
    }
}