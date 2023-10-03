import java.util.Scanner;

/**
 * LC209MinimumSizeSubarraySum
 */
public class LC209MinimumSizeSubarraySum {
    public static int minSubArrayLen(int target, int[] nums) {
        int back = 0, front = 0, length = 100001;

        int sum = nums[0];
        while (front < nums.length) {
            if (sum < target) {
                front++;
                if (front < nums.length) {
                    sum += nums[front];
                }
            } else if (sum >= target) {
                int l = front - back + 1;
                if (l < length) {
                    length = l;
                }
                sum -= nums[back];
                back++;
            }
        }

        if (length == 100001) {
            return 0;
        }
        return length;
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

        System.out.print("Enter atrget number: ");
        int target = scan.nextInt();

        scan.close();
        int size = minSubArrayLen(target, arr);
        System.out.println(size);
    }
}