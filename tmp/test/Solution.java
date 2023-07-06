package tmp.test;

import java.util.Scanner;

/**
 * Solution
 */
public class Solution {
    public static int countCustomers(int[] bill) {
        int answer = 0;
        // write your code here

        for (int i = 0; i < bill.length; i++) {
            double sqrt = Math.sqrt(bill[i]);

            if ((sqrt - Math.floor(sqrt)) == 0) {
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // input for bill
        int bill_size = in.nextInt();
        int bill[] = new int[bill_size];
        for (int idx = 0; idx < bill_size; idx++) {
            bill[idx] = in.nextInt();
        }

        int result = countCustomers(bill);
        System.out.println(result);
    }
}