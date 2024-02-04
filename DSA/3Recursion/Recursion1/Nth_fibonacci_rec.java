
// the program will not work for large numbers
import java.util.Scanner;

/**
 * fibonacci_rec
 */
public class Nth_fibonacci_rec {
    public static long fibonacci(int n) {
        if (n == 1 || n == 2) {
            return 1;
        }

        return (Long) fibonacci(n - 1) + (Long) fibonacci(n - 2);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        System.out.println(n + "th/rd fibonacci number = " + fibonacci(n));
    }
}