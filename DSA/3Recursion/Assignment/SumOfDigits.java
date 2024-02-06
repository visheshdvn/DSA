import java.util.Scanner;

public class SumOfDigits {

    public static int sumOfDigits(int n) {
        if (n == 0) {
            return n;
        }

        return n%10 + sumOfDigits(n/10);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = scan.nextInt();
        scan.close();

        System.out.println("Sum of digits of number = " + sumOfDigits(n));
    }
}
