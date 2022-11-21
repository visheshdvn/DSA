package tmp;

import java.util.*;

public class Test {
    static int reverse(int n) {
        int ans = 0, bits = 0;

        while (bits < 32) {
            ans <<= 1;
            if ((bits & 1) == 1) {
                ans += 1;
            }
            n >>= 1;
            bits += 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        scan.close();

        // System.out.println(reverse(n));
    }
}
