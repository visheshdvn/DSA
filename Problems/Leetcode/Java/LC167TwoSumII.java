import java.util.Scanner;

/**
 * LC167TwoSumII
 */
public class LC167TwoSumII {

    public static int[] twoSum(int[] numbers, int target) {
        int first = 0, last = numbers.length - 1;

        while (first < last) {
            int sum = numbers[first] + numbers[last];

            if (sum < target) {
                first++;
            } else if (sum > target) {
                last--;
            } else if (sum == target) {
                int[] arr = { first, last };
                return arr;
            }
        }

        return new int[2];
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
        int[] size = twoSum(arr, target);
        printArr(size, 0, size.length);
    }
}