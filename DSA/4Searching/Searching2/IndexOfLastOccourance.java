import java.util.Scanner;

public class IndexOfLastOccourance {

    public static int indexOfLastOccourance(int[] arr, int elem) {
        int start = 0, last = arr.length - 1;

        while (start <= last) {
            int mid = start + (last - start) / 2;

            if (arr[mid] < elem) {
                start = mid + 1;
            } else if (arr[mid] > elem) {
                last = mid - 1;
            } else {
                if (mid == arr.length - 1 || arr[mid + 1] != elem) {
                    return mid;
                } else {
                    start = mid + 1;
                }
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
        int index = indexOfLastOccourance(arr, scan.nextInt());
        scan.close();

        System.out.println("Index of element: " + index);
    }
}
