import java.util.Scanner;

public class LC242ValidAnagram {
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int chars[] = new int[26];

        for (char i : s.toCharArray()) {
            chars[i - 'a']++;
        }

        for (char i : t.toCharArray()) {
            chars[i - 'a']--;
        }

        for (int i : chars) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter string one: ");
        String s = scan.nextLine();

        System.out.println("Enter string two: ");
        String t = scan.nextLine();

        scan.close();
        System.out.println(isAnagram(s, t));
    }
}
