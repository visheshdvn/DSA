import java.util.Scanner;

public class MoveZeroes {

    public static void moveZeroes(int[] nums) {
        if (nums.length == 1) {
            return;
        }

        int i = 0, j = 0;

        while (j < nums.length) {
            if (i == j && nums[i] != 0) {
                i += 1;
                j += 1;
            } else if (i == j && nums[i] == 0) {
                j += 1;
            } else if (i != j && nums[i] == 0 && nums[j] != 0) {
                nums[i] = nums[j];
                nums[j] = 0;
                i += 1;
                j += 1;
            } else if (i != j && nums[i] == 0 && nums[j] == 0) {
                j += 1;
            } else if (i != j && nums[i] != 0 && nums[j] == 0) {
                i += 1;
                j += 1;
            } else if (i != j && nums[i] != 0 && nums[j] != 0) {
                i += 1;
            }
        }

    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
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

        moveZeroes(arr);
        printArray(arr);
    }
}
