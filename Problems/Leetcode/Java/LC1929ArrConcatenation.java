import java.util.Scanner;

public class LC1929ArrConcatenation {
    public static int[] getConcatenation(int[] nums) {
        int a[] = new int[nums.length * 2];
        for (int i = 0; i < nums.length; i++) {
            a[i] = nums[i];
            a[nums.length + i] = nums[i];
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.println("Enter values: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        scan.close();
        // System.out.println("", getConcatenation(arr));
        for (int i : getConcatenation(arr)) {
            System.out.println(i);
        }
    }
}
