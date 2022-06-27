import java.util.Scanner;

public class PalindromeString {

    public static boolean isPalindrome(String str) {
        int i = 0, n = str.length();
        boolean result = true;
        // System.out.println("Length: " + str.length() + "\n" + "Half:" + str.length()
        // / 2);

        while (i < n / 2) {
            result = result && str.charAt(i) == str.charAt(n - 1 - i);
            i++;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String s = scan.nextLine();

        scan.close();
        System.out.println("String entered: " + s);
        System.out.println("Palindrome: " + isPalindrome(s));
    }
}
