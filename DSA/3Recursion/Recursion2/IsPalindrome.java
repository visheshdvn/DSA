import java.util.Scanner;

public class IsPalindrome {

    public static boolean isPalindrome(String str, int start, int end) {
        if (start >= end) {
            return true;
        }

        return str.charAt(start) == str.charAt(end) && isPalindrome(str, start + 1, end - 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        scan.close();

        System.out.println(isPalindrome(str, 0, str.length() - 1));
    }
}
