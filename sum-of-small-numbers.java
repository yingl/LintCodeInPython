// Only java code

import java.util.*;

public class Main {
	public static void main(String[] args){
        // write your code here
        int ret = 0;
        int max = Integer.MIN_VALUE;
        int c = 0;
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 0; i < n; ++i) {
            int v = scanner.nextInt();
            ret += v;
            if (v > max) {
                max = v;
                c = 1;
            } else if (v == max) {
                ++c;
            }
        }
        System.out.println(ret - max * c);
  }
}

// easy: https://www.lintcode.com/problem/2820
