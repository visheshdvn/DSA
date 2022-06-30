import java.util.Scanner;

public class CountNoOfOneInSortedBinaryArray {

    public static int numberOfOnes(int[] arr) {
        int elem = 1;
        int start = 0, last = arr.length - 1, firstIndex = arr.length;

        while (start <= last) {
            int mid = start + (last - start) / 2;

            if (arr[mid] < elem) {
                start = mid + 1;
            } else if (arr[mid] > elem) {
                last = mid - 1;
            } else {
                if (mid == 0 || arr[mid - 1] != elem) {
                    firstIndex = mid;
                    break;
                } else {
                    last = mid - 1;
                }
            }
        }

        return arr.length - firstIndex;
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

        int nos = numberOfOnes(arr);
        scan.close();

        System.out.println("Index of element: " + nos);
    }
}
