import java.util.Scanner;

/**
 * replaceAbyB
 */
public class ReplaceAbyB {
    public static String replaceHelper(String s, char a, char b, int i) {
        if (s.length() == 0 || i >= s.length()) {
            return "";
        }

        if (s.charAt(i) == a) {
            return b + replaceHelper(s, a, b, i+1);
        } else {
            return s.charAt(i) + replaceHelper(s, a, b, i+1);
        }
    }

    public static String replace(String s, char a, char b) {
        return replaceHelper(s, a, b, 0);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String s = scan.nextLine();

        System.out.print("Enter char a: ");
        char a = scan.next().charAt(0);

        System.out.print("Enter char b: ");
        char b = scan.next().charAt(0);

        scan.close();
        
        System.out.println("New String: " + replace(s, a, b));
    }
}