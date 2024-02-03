import java.util.Arrays;
import java.util.Scanner;
/**
 * LC1051HeightChecker
 */
public class LC1051HeightChecker {
    public static int heightChecker(int[] heights) {
        int[] correctPositions = new int[heights.length];

        int i = 0;
        while (i<heights.length) {
            correctPositions[i] = heights[i];
            i++;
        }

        Arrays.sort(correctPositions);

        int n = 0, count = 0;
        while (n < heights.length) {
            if (heights[n] != correctPositions[n]) {
                count++;
            }
            n++;
        }

        return count;
    }

    // take element input
    public static void populateArr(int[] arr, int startIndex, int n) {
        // populates n numbers from startIndex
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < startIndex + n; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static void printArr(int[] arr, int startIndex, int n) {
        // prints n numbers from startIndex
        for (int i = startIndex; i < startIndex + n && i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.println("Enter values: ");
        populateArr(arr, 0, n);
        scan.close();

        int res = heightChecker(arr);
        System.out.println(res);
    }
}