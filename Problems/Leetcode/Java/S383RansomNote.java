import java.util.HashMap;
import java.util.Scanner;

public class S383RansomNote {
    public static boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> h = new HashMap<>();

        for (int i = 0; i < magazine.length(); i++) {
            char c = magazine.charAt(i);
            h.put(c, h.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            char c = ransomNote.charAt(i);
            int count = h.getOrDefault(c, 0);
            if (count == 0) {
                return false;
            } else {
                h.put(c, count - 1);
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String ransomNote = scan.nextLine();
        String magazine = scan.nextLine();
        scan.close();
        System.out.println(canConstruct(ransomNote, magazine));
    }
}
