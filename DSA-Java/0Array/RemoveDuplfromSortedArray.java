import java.util.Scanner;

public class RemoveDuplfromSortedArray {
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 1) {
            return 1;
        }

        int curr = 1, n = 1;

        while (n < nums.length) {
            if (curr == n && nums[curr] != nums[curr - 1]) {
                nums[curr] = nums[n];
                curr += 1;
            } else if (curr != n && nums[curr] != nums[n]) {
                if (!(nums[n] == nums[curr - 1])) {
                    nums[curr] = nums[n];
                    curr += 1;
                }
            }
            n += 1;
        }

        return curr;
    }

    private static void printNewArray(int[] arr, int n) {

        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter Size of array");
        int n = scan.nextInt();
        int arr[] = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();
        // System.out.println(removeDuplicates(arr));
        printNewArray(arr, removeDuplicates(arr));
    }
}
