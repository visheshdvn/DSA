import java.util.Scanner;

/**
 * LC151ReverseWWordsInString
 */
public class LC151ReverseWWordsInString {
    public static String reverseWords(String s) {
        s = s.strip();
        String[] arr = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for (int i = arr.length - 1; i >= 0; i--) {
            // System.out.println(arr[i]);
            if (arr[i].strip() != "") {
                sb.append(arr[i]).append(" ");
            }
        }

        return sb.toString().strip();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String s = scan.nextLine();

        System.out.println(reverseWords(s));
    }
}