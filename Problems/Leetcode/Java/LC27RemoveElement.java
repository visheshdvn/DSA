import java.util.Scanner;

public class LC27RemoveElement {
    // method 1
    public static int removeElement(int[] nums, int val) {
        int slow = 0, fast = 0;

        while (fast < nums.length) {
            if (nums[fast] != val && nums[slow] != val) {
                slow++;
            } else if (nums[slow] == val && nums[fast] != val) {
                nums[slow] = nums[fast];
                nums[fast] = val;
                slow++;
            }

            fast++;
        }

        return slow;
    }

    // method 2
    public static int removeElement2(int[] nums, int val) {
        int slow = 0, fast = 0;

        while (fast < nums.length) {
            if (nums[fast] != val) {
                nums[slow] = nums[fast];
                slow++;
            }
            fast++;
        }
        return slow;
    }

    // take element input
    public static void populateArr(int[] arr, int startIndex, int length) {
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < startIndex + length; i++) {
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

        System.out.print("Enter the number to eliminate: ");
        int val = scan.nextInt();

        int size = removeElement(arr, val);
        printArr(arr, 0, size);
    }
}