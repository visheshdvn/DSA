import java.util.Scanner;

public class BinarySearch {
    public static int binarySearch(int[] input, int elem) {
        int start = 0;
        int last = input.length - 1;

        while (start <= last) {
            int mid = start + (last - start) / 2;
            if (elem == input[mid]) {
                return mid;
            } else if (elem > input[mid]) {
                start = mid + 1;
            } else {
                last = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.print("Enter elements of array in sorted form (ASC): ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        System.out.print("Enter element to find: ");
        int index = binarySearch(arr, scan.nextInt());
        scan.close();

        System.out.println("Index of element: " + index);
    }
}
