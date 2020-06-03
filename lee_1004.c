#define max(a, b) (a) > (b) ? (a) : (b)
int longestOnes(int* A, int ASize, int K){
    int ans = 0;
    int left, cumNum;
    left = cumNum = 0;
    for (int i = 0; i < ASize; i++) {
        if (A[i] == 0) {
            cumNum++;
        }
        while (cumNum > K) {
            if (A[left++] == 0) {
                cumNum--;
            }
        }
        ans = max(ans, i - left + 1);
    }
    return ans;
}



