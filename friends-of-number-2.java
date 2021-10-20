// Only java code

public class Solution {
    public static boolean isFriend(int n) {
        // write your code here
        int r = 0;
        while (n > 0) {
            if ((n % 2) == 1) {
                ++r;
            }
            n /= 2;
        }
        return r == 2;
    }
}

// easy: https://www.lintcode.com/problem/2826
