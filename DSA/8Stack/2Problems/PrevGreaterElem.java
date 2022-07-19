import java.util.ArrayDeque;
import java.util.Scanner;

public class PrevGreaterElem {
    static void prevGreaterElements(int[] arr) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int i : arr) {
            while (!stack.isEmpty() && stack.peek() < i) {
                stack.pop();
            }

            if (stack.isEmpty()) {
                System.out.print(-1 + " ");
            } else {
                System.out.print(stack.peek() + " ");
            }

            stack.push(i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int[] arr = new int[sc.nextInt()];

        System.out.print("Enter values: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        prevGreaterElements(arr);
    }
}
