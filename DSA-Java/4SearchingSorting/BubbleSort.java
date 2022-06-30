import java.util.Scanner;

public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int k = arr.length - 1;

        while (k > 0) {
            int j = 0;
            while (j < k) {
                if (arr[j] > arr[j + 1]) {
                    int t = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = t;
                }
                j += 1;
            }
            k -= 1;
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

        System.out.print("Enter elements of array in sorted form (ASC): ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();
        bubbleSort(arr);
        printArray(arr);
    }
}
