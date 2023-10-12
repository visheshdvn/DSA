import java.util.Scanner;

/**
 * LC557ReverseWordsInString
 */
public class LC557ReverseWordsInString {

    public static String reverseWord(String s) {
        char[] carr = s.toCharArray();
        int n = carr.length - 1;

        for (int i = 0; i < carr.length / 2; i++) {
            char c = carr[i];
            carr[i] = carr[n - i];
            carr[n - i] = c;
        }

        return new String(carr);
    }

    public static String reverseWords(String s) {
        String[] arr = s.split(" ");

        for (int i = 0; i < arr.length; i++) {
            arr[i] = reverseWord(arr[i]);
        }

        return String.join(" ", arr);
    }

    // slightly more optimized thanabove implementation
    public static String reverseWords2(String s) {
        String rs = reverseWord(s);
        String[] sarr = rs.split(" ");
        StringBuilder sb = new StringBuilder();

        for (int i = sarr.length - 1; i > 0; i--) {
            sb.append(sarr[i]).append(" ");
        }

        sb.append(sarr[0]);

        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter the string: ");
        String s = scan.nextLine();
        scan.close();

        System.out.println("Output: " + reverseWords2(s));
    }
}