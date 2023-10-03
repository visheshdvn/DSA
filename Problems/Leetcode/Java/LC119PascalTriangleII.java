import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * LC119PascalTriangleII
 */
public class LC119PascalTriangleII {
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

    public static List<Integer> getRow(int rowIndex) {
        List<Integer> list = new ArrayList<>();
        int[] l = new int[rowIndex + 1];

        for (int i = 0; i <= rowIndex / 2; i++) {
            l[i] = l[rowIndex - i] = nCr(rowIndex, i);
        }

        for (int i : l) {
            list.add(i);
        }
        return list;
    }

    public static void printList(List<Integer> l) {
        for (int i = 0; i < l.size(); i++) {
            System.out.print(l.get(i) + " ");
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter value of n: ");
        int n = scan.nextInt();
        scan.close();

        List<Integer> l = getRow(n);

        printList(l);
    }
}