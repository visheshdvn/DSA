import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * LC66PlusOne
 */
public class LC54SpiralMatrix {

    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> nums = new ArrayList<Integer>();

        // int h1 = 0, h2 = matrix.length;
        // int v1 = 0, v2 = matrix[0].length;

        int rowJump = matrix.length - 1;
        int colJump = matrix[0].length - 1;

        int row = 0, col = 0;

        while (rowJump > 0 || colJump > 0) {
            // int i = 0, j = 0;
            // take coljump first
            // while (i <= colJump) {
            // System.out.print(matrix[j][i] + " ");
            // i++;
            // }
            // i--;
            // j++;

            // take row jump
            // while (j <= rowJump) {
            // System.out.print(matrix[j][i] + " ");
            // j++;
            // }
            // j--;
            // i--;

            // reverse direction
            // colJump--;
            // rowJump--;

            // take col jump
            for (int i = 0; i <= colJump; i++) {
                System.out.print(matrix[row][col] + " ");
                col++;
            }
            col--;
            row++;

            // take row jump
            for (int i = 0; i < rowJump; i++) {
                System.out.print(matrix[row][col] + " ");
                row++;
            }
            row--;
            col--;

            // reverse dir
            colJump--;
            rowJump--;

            // reverse col jump
            for (int i = 0; i <= colJump; i++) {
                System.out.print(matrix[row][col] + " ");
                col--;
            }
            col++;
            row--;

            // reverse row jump
            for (int i = 0; i < rowJump; i++) {
                System.out.print(matrix[row][col] + " ");
                row--;
            }
            row++;
            col++;

            colJump--;
            rowJump--;
            // break;
        }

        if (rowJump == 0 && colJump == 0) {
            System.out.println(matrix[row][col]);
        }

        return nums;
    }

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

    public static void print2DArray(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int i = scan.nextInt();
        System.out.print("Enter number of cols: ");
        int j = scan.nextInt();

        int[][] arr = new int[i][j];

        System.out.println("Enter elements of array: ");
        for (int k = 0; k < arr.length; k++) {
            int[] col = new int[j];
            populateArr(col, 0, j);
            arr[k] = col;
        }

        spiralOrder(arr);

        // print2DArray(arr);
    }
}