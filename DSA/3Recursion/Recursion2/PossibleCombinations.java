import java.util.Scanner;

public class PossibleCombinations {
    public static int combinations(int l, int a, int b, int c) {
        if (l == 0) {
            return 1;
        }

        if (l < a && l < b && l < c) {
            return 0;
        }

        return combinations(l - a, a, b, c) + combinations(l - b, a, b, c) + combinations(l - c, a, b, c);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter length of rope");
        int l = scan.nextInt();

        System.out.println("Enter length of 3 pieces");
        int a = scan.nextInt(), b = scan.nextInt(), c = scan.nextInt();
        scan.close();

        System.out.println("Possible Combinations = " + combinations(l, a, b, c));
    }
}
