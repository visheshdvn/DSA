import java.util.Scanner;

public class LargestElement {

    public static int getLargestElement(int[] arr, int n) {
        int elem = Integer.MIN_VALUE;

        for (int i : arr) {
            if (i > elem)
                elem = i;
        }

        return elem;
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

        System.out.println(getLargestElement(arr, n));
    }
}
