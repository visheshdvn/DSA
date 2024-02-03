import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

/**
 * Solution
 */
public class Solution {

    public static int[] solution(int area) {
        List<Integer> list = new ArrayList<>();

        while (area > 0) {
            int root = (int) Math.floor(Math.sqrt(area));
            int substraction = root * root;
            list.add(substraction);
            area -= substraction;
        }

        int[] arr = list.stream().mapToInt(i->i).toArray();

        return arr;
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

        // [1, 1000000]
        System.out.print("Enter area [1, 1000000]: ");
        int area = scan.nextInt();

        int[] ans = solution(area);
        printArr(ans, 0, ans.length);
    }
}