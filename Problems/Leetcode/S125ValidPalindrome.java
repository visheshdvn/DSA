import java.util.Scanner;

public class S125ValidPalindrome {

    public static boolean isPalindrome(String s) {
        int i = 0, j = s.length()-1;

        s = s.toLowerCase();

        while (j>=i) {
            int back = (int) s.charAt(i);
            int front = (int) s.charAt(j);
            if ((97 <= back && back <= 122 && 97 <= front && front <= 122) || (48 <= back && back <= 57 && 48 <= front && front <= 57)) {
                if (back != front) {
                    return false;
                }
                i++;
                j--;
            }

            if (back < 48 || 122 < back || (57 < back && back < 97)) {
                i++;
            }

            if (front < 48 || 122 < front || (57 < front && front < 97)) {
                j--;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        System.out.print(isPalindrome(s));

    }
}
