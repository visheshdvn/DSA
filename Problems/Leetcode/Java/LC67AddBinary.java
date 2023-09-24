import java.util.Scanner;

/**
 * LC67AddBinary
 */
public class LC67AddBinary {
    public static String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0) {
                carry += a.charAt(i--) - '0';
            }
            if (j >= 0) {
                carry += b.charAt(j--) - '0';
            }
            sb.append(carry % 2);
            carry /= 2;
        }

        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter binary string one: ");
        String s1 = scan.nextLine();
        System.out.print("Enter binary string two: ");
        String s2 = scan.nextLine();

        System.out.println(addBinary(s1, s2));
    }
}