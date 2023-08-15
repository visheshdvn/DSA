import java.util.Scanner;

public class LC905SortArrByParity {
    public static int[] sortArrayByParity(int[] nums) {
        int n = 0, curr = 0;

        while (n < nums.length) {
            if ((nums[n] & 1) == 0) {
                int e = nums[curr];
                nums[curr] = nums[n];
                nums[n] = e;

                curr++;
            }

            n++;
        }

        return nums;
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

        int[] res = sortArrayByParity(arr);
        printArr(arr, 0, res.length);
    }
}
