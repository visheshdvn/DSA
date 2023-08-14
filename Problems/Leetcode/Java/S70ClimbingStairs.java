import java.util.Scanner;

public class S70ClimbingStairs {
    public static int climbStairs(int n) {
        if (n < 2) {
            return 1;
        }
        int first = 1, second = 1, front = 0;
        for (int i = 2; i <= n; i++) {
            front = first + second;
            first = second;
            second = front;
        }
        return front;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter value of n");
        int n = scan.nextInt();
        scan.close();
        climbStairs(n);
    }
}
