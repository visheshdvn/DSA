import java.util.Scanner;

/**
 * LC198RotateArray
 */
public class LC198RotateArray {

    public static void rotate_helper(int[] nums, int s, int e) {
        int start = s, end = e - 1;

        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;

            start++;
            end--;
        }
    }

    public static void rotate(int[] nums, int k) {
        int n = k % nums.length;
        rotate_helper(nums, 0, nums.length);
        rotate_helper(nums, 0, n);
        rotate_helper(nums, n, nums.length);
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

        System.out.print("Enter the elements to rotate: ");
        int k = scan.nextInt();
        rotate(arr, k);
        printArr(arr, 0, arr.length);
    }
}