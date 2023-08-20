import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * LC448FindAllNosDisappearedInArr
 */
public class LC448FindAllNosDisappearedInArr {
    public static List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> disappeared = new ArrayList<Integer>();

        int n = 0;
        while (n < nums.length) {
            int index = Math.abs(nums[n]) - 1;
            nums[index] = -1 * Math.abs(nums[index]);
            n++;
        }

        int k = 0;
        while (k < nums.length) {
            if (nums[k] > 0) {
                disappeared.add(k + 1);
            }

            k++;
        }

        return disappeared;
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

        List<Integer> res = findDisappearedNumbers(arr);
        int i = 0;
        while (i < res.size()) {
            System.out.print(res.get(i) + " ");
            i++;
        }
    }
}