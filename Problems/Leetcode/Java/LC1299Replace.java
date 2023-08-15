import java.util.Scanner;

public class LC1299Replace {

    public static int[] replaceElements(int[] arr) {
        if (arr.length == 1) {
            int a[] = { -1 };
            return a;
        }

        int ans[] = new int[arr.length];
        int k = ans.length - 1;
        ans[k] = -1;

        for (int i = arr.length - 1; i > 0; i--) {
            if (arr[i] > ans[k]) {
                k--;
                ans[k] = arr[i];
            } else {
                k--;
                ans[k] = ans[k + 1];
            }
        }

        return ans;
    }

    public static int[] replaceElements2(int[] arr) {
        if (arr.length == 1) {
            int a[] = { -1 };
            return a;
        }

        int n = arr.length - 1;
        int max = -1;

        while (n >= 0) {
            if (arr[n] > max) {
                int nextMax = arr[n];
                arr[n] = max;
                max = nextMax;
            } else {
                arr[n] = max;
            }

            n--;
        }

        return arr;
    }

    // take element input
    public static void populateArr(int[] arr, int startIndex, int n) {
        // populates n numbers from startIndex
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < startIndex + n; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static void printArr(int[] arr, int startIndex, int n) {
        // prints n numbers from startIndex
        for (int i = startIndex; i < startIndex + n && i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.println("Enter values: ");
        populateArr(arr, 0, n);
        scan.close();

        int res[] = replaceElements2(arr);
        printArr(res, 0, n);
    }
}
