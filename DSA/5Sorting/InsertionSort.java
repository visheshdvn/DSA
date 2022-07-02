import java.util.Scanner;

public class InsertionSort {

    public static void bubbleSort(int[] arr) {
        if (arr.length <= 1) {
            return;
        }

        for (int i = 1; i < arr.length; i++) {
            int num = arr[i];
            int j = i - 1;

            while ((j >= 0) && arr[j] > num) {
                arr[j + 1] = arr[j];
                j -= 1;
            }

            arr[j + 1] = num;
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

        System.out.print("Enter elements in array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();

        bubbleSort(arr);
        printArray(arr);
    }
}
