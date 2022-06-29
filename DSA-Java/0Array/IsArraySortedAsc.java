import java.util.Scanner;

public class IsArraySortedAsc {

    public static boolean isSorted(int[] arr, int n) {
        boolean sorted = true;

        for (int i = 0; i < n - 1; i++) {
            sorted = sorted && (arr[i] < arr[i + 1]);
        }
        return sorted;
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

        System.out.print("" + isSorted(arr, n));
    }
}
