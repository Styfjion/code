class Solution {
public:
    int NumberOf1(int n) {
        int sum = 0;
        while(n)
        {
            n = (n-1)&n;
            sum++;
        }
        return sum;
    }
};