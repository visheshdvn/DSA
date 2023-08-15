import java.util.Hashtable;
import java.util.Scanner;

public class LC941ValidMountArr {
    public static boolean validMountainArray(int[] arr) {
        if (arr.length < 3) {
            return false;
        }

        boolean flipped = false;
        int uphillSteps = 0, downhillSteps = 0;

        int n = 1;
        while (n < arr.length) {
            if (arr[n - 1] > arr[n] && !flipped) {
                flipped = true;
            }

            if ((flipped && arr[n - 1] <= arr[n]) || (!flipped && arr[n - 1] == arr[n])) {
                return false;
            }

            if (!flipped) {
                uphillSteps++;
            } else {
                downhillSteps++;
            }
            n++;
        }

        return uphillSteps > 0 && downhillSteps > 0;
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
        System.out.print("length of array: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.print("Enter elements of array: ");
        populateArr(arr, 0, n); // populates array from [startIndex, startIndex+length) position

        boolean res = validMountainArray(arr);
        // printArr(arr, 0, size);
        System.out.println(res);
    }
}
