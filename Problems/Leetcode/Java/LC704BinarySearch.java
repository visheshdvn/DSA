import java.util.Scanner;

public class LC704BinarySearch {

    public static int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.print("Enter values: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        System.out.print("Enter number to find: ");
        int target = scan.nextInt();

        scan.close();
        System.out.print("Position of target element: " + search(arr, target));
    }
}
