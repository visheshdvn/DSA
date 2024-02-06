import java.util.Scanner;

public class NumberOfDigits {
    public static int numberOfDigits(int n) {
        n = Math.abs(n);
        int count = 0;

        while (n>0) {
            count++;
            n/=10;
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = scan.nextInt();
        scan.close();

        System.out.println("Nmebr of digits = " + numberOfDigits(n));
    }
}
