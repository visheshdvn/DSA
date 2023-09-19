import java.util.Scanner;

/**
 * LC747LargestNoTwiceOfOthers
 */
public class LC747LargestNoTwiceOfOthers {
    public static int dominantIndex(int[] nums) {
        int first = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        int maxInd = -1;

        for (int i = 0; i < nums.length; i++) {
            if (first < nums[i]) {
                second = first;
                first = nums[i];
                maxInd = i;
            } else if (second < nums[i]) {
                second = nums[i];
            }
        }

        if (first >= 2 * second) {
            return maxInd;
        } else {
            return -1;
        }
    }

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

        int res = dominantIndex(arr);
        System.out.println(res);
    }

}