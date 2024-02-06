import java.util.Scanner;

public class StringToInteger {

    public static int stringToIntegerHelper(String s, int i) {
        if (i < 0 || i >= s.length()) {
            return 0;
        }

        int ones = s.charAt(i) - '0';

        int smallN = stringToIntegerHelper(s, i - 1);

        return 10 * smallN + ones;
    }

    public static int stringToInteger(String s) {
        return stringToIntegerHelper(s, s.length() - 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a numeric string (e.g. 12345): ");
        String s = scan.nextLine();
        scan.close();

        System.out.println("int value = " + stringToInteger(s));
    }
}
