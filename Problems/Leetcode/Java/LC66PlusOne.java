import java.util.Scanner;

/**
 * LC66PlusOne
 */
public class LC66PlusOne {
    public static int[] plusOne(int[] digits) {
        int carry = 1, i = digits.length - 1;

        while (i >= 0) {
            int sum = carry + digits[i];
            digits[i] = sum % 10;
            carry = sum / 10;
            i--;
        }

        if (carry == 1) {
            int nums[] = new int[digits.length + 1];
            nums[0] = 1;

            int j = 1;
            while (j < nums.length) {
                nums[j] = digits[j - 1];
                j++;
            }

            return nums;
        }

        return digits;
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

        int[] res = plusOne(arr);
        printArr(res, 0, res.length);
    }
}