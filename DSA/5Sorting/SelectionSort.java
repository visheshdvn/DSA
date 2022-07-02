import java.util.Scanner;

public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int curr = 0;

        while (curr < arr.length) {
            int min_ind = curr;
            for (int i = min_ind + 1; i < arr.length; i++) {
                if (arr[i] < arr[min_ind]) min_ind = i;
            }

            if (min_ind != curr) {
                int t = arr[curr];
                arr[curr] = arr[min_ind];
                arr[min_ind] = t;
            }
            curr += 1;
        }
    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.print("Enter elements of array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();
        selectionSort(arr);
        printArray(arr);
    }
}
