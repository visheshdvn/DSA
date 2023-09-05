import java.util.Arrays;
import java.util.Scanner;

/**
 * LC344ReverseString
 */
public class LC344ReverseString {

    public static void helper(int n, char[] arr) {
        if(n >= arr.length) {
            return;
        }

        char c = arr[n];
        helper(n+1, arr);

        arr[arr.length -1-n] = c;
    }

    public static void reverseStringRecursive(char[] s) {
        if (s.length < 2) {
            return;
        }

        helper(0, s);
    }

    public static void populateArr(char[] arr, int startIndex, int n) {
        // populates n numbers from startIndex
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < startIndex + n; i++) {
            arr[i] = scan.next().charAt(0);
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter length of array: ");
        char[] arr = new char[scan.nextInt()];

        populateArr(arr, 0, arr.length);
        scan.close();

        reverseStringRecursive(arr);
        System.out.println(Arrays.toString(arr));
    }
}