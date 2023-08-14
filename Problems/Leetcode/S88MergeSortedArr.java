import java.util.Scanner;

/**
 * S88MergeSortedArr
 */
public class S88MergeSortedArr {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = nums1.length - 1,
                a = m - 1,
                b = n - 1;
        
        while (a >= 0 && b>=0) {
            if (nums2[b] > nums1[a]) {
                nums1[index] = nums2[b];
                b--;
            } else {
                nums1[index] = nums1[a];
                a--;
            }
            index--;
        }

        while (b>=0) {
            nums1[index] = nums2[b];
            b--;
            index--;
        }
    }

    // take element input
    public static void populateArr(int[] arr, int startIndex, int length) {
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < length; i++) {
            arr[i] = scan.nextInt();
        }
        scan.close();
    }

    public static void printArr(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("length of l1: ");
        int n = scan.nextInt();
        int arr1[] = new int[n];

        System.out.print("Numbers of elements in array 1: ");
        int n1 = scan.nextInt();
        scan.close();

        System.out.print("Enter arr1 elements: ");
        populateArr(arr1, 0, n1);

        int arr2[] = new int[n - n1];
        System.out.print("Enter arr2 elements: ");
        populateArr(arr2, 0, n - n1);

        merge(arr1, n1, arr2, n - n1);
        printArr(arr1);
        // printArr(arr2);
    }
}