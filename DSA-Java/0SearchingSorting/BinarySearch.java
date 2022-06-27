import java.util.Scanner;

public class BinarySearch {
    public static int binarySearch(int[] input, int elem) {
        int start = 0;
        int last = input.length - 1;

        while (start <= last) {
            int mid = (start + last) / 2;
            if (elem == input[mid]) {
                return mid;
            } else if (elem > input[mid]) {
                start = mid + 1;
            } else {
                last = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int input[] = { 2, 3, 4, 5, 6, 7, 8, 9 };

        Scanner scan = new Scanner(System.in);
        int index = binarySearch(input, scan.nextInt());
        scan.close();
        System.out.println(index);
    }
}
