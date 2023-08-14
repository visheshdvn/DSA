import java.util.Scanner;

/**
 * S88MergeSortedArr
 */
public class S88MergeSortedArr {

    // take element input
    public void populateArr(int[] arr, int startIndex, int length) {
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < endIndex; i++) {
            arr[i] = scan.nextInt();
        }
        scan.close();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("length of l1: ");
        int n = scan.nextInt();

        System.out.println("Numbers of elements in array 1");
        int n1 = scan.nextInt();

        int arr[] = new int[n];
        System.out.print("Enter arr elements: ");
        populateArr(arr, 0, n1)
    }
}