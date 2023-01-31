import java.util.Scanner;

public class S680CalidPalindromeII {
    static public boolean validPalindromeHelper(String s, int left, int right, boolean isDeleted) {
        while (left <= right) {
            if (s.charAt(left) != s.charAt(right)) {
                if (isDeleted) {
                    return false;
                }

                return validPalindromeHelper(s, left + 1, right, true)
                        || validPalindromeHelper(s, left, right - 1, true);
            }

            left++;
            right--;
        }
        return true;
    }

    static public boolean validPalindrome(String s) {
        if (s == "" || s.length() == 1) {
            return true;
        }

        return validPalindromeHelper(s, 0, s.length() - 1, false);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String s = scan.nextLine();
        scan.close();

        System.out.print("" + validPalindrome(s));
    }
}

// abcbxa
// axkbcba