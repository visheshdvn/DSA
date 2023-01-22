import java.util.Scanner;

public class S1299Replace {

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

        int res[] = replaceElements(arr);

        for (int i : res) {
            System.out.print(i + " ");
        }
    }
}
