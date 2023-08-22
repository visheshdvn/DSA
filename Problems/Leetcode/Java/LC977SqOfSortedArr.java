import java.util.Scanner;

/**
 * LC977SqOfSortedArr
 */
public class LC977SqOfSortedArr {
    public static int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];

        int front = n - 1, back = 0, index = n - 1;

        while (back <= front) {
            int l_sq = nums[back] * nums[back];
            int r_sq = nums[front] * nums[front];

            if (l_sq < r_sq) {
                res[index] = r_sq;
                front--;
            } else {
                res[index] = l_sq;
                back++;
            }

            index--;
        }

        return res;
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

        scan.close();
        int[] res = sortedSquares(arr);
        printArr(res, 0, n);
    }
}