import java.util.Scanner;

public class LC26RemoveDuplFromSortedArr {
    public static int removeDuplicates(int[] nums) {
        int last = -101, curr = 0, n = 0;

        while (n < nums.length) {
            if (nums[n] != last) {
                nums[curr] = nums[n];
                last = nums[n];
                curr++;
            }
            n++;
        }
        return curr;
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

        int size = removeDuplicates(arr);
        printArr(arr, 0, size);
    }
}