import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * LC66PlusOne
 */
public class LC54SpiralMatrix {
    public static List<Integer> spiralOrder(int[][] matrix) {
        int i = 0, j = 0;
        List<Integer> list = new ArrayList<>();

        while (i < matrix.length && j < matrix[0].length) {
            int move = 0;
            while (j < matrix[i].length) {
                if (matrix[i][j] == -101) {
                    break;
                }
                list.add(matrix[i][j]);
                matrix[i][j] = -101;
                j++;
                move++;
            }
            j--;
            i++;

            while (i < matrix.length) {
                if (matrix[i][j] == -101) {
                    break;
                }
                list.add(matrix[i][j]);
                matrix[i][j] = -101;
                i++;
                move++;
            }
            i--;
            j--;

            // reverse the order

            while (j >= 0) {
                if (matrix[i][j] == -101) {
                    break;
                }
                list.add(matrix[i][j]);
                matrix[i][j] = -101;
                j--;
            }
            j++;
            i--;

            while (i >= 0) {
                if (matrix[i][j] == -101) {
                    break;
                }
                list.add(matrix[i][j]);
                matrix[i][j] = -101;
                i--;
            }
            i++;
            j++;

            if (move == 0) {
                break;
            }
        }

        return list;
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