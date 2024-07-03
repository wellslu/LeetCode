class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {
            n = abs(n);
            x = 1 / x;
        }
        double answer = 1;
        while (n > 0) {
            if (n % 2 != 0) {
                answer*=x;
            }
            x*=x;
            // bit位移會快很多
            // n/=2;
            n >>= 1;
        }
        return answer;
    }
};
