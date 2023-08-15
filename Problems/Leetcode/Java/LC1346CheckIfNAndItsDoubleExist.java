import java.util.Hashtable;
import java.util.Scanner;

public class LC1346CheckIfNAndItsDoubleExist {
    public static boolean checkIfExist(int[] arr) {
        Hashtable<Integer, Boolean> ht = new Hashtable<Integer, Boolean>();

        int n = 0;
        while (n < arr.length) {
            if (ht.containsKey(arr[n] * 2) || ((arr[n] & 1) != 1 ? ht.containsKey(arr[n] / 2) : false)) {
                return true;
            } else {
                ht.put(arr[n], true);
            }
            n++;
        }

        return false;
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

        boolean res = checkIfExist(arr);
        // printArr(arr, 0, size);
        System.out.println(res);
    }
}
