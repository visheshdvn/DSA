import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * LC118PascalsTriangle
 */
public class LC118PascalsTriangle {
    static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    public static int nCr(int n, int r) {
        if (n == 0) {
            return 1;
        }

        if (r > n / 2) {
            r = n - r;
        }

        int num = 1, den = 1;
        while (r > 0) {
            num *= n;

            if (num % r != 0) {
                den *= r;
            } else {
                num /= r;
            }

            int gcd = gcd(num, den);
            num /= gcd;
            den /= gcd;

            n--;
            r--;
        }

        return num / den;
    }

    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            List<Integer> l = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                l.add(nCr(i, j));
            }
            list.add(l);
        }

        return list;
    }

    public static void printListOfList(List<List<Integer>> l) {
        for (int i = 0; i < l.size(); i++) {
            List<Integer> subList = l.get(i);
            for (int j = 0; j < subList.size(); j++) {
                System.out.print(subList.get(j) + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter value of n: ");
        int n = scan.nextInt();

        List<List<Integer>> l = generate(n);
        printListOfList(l);

    }
}