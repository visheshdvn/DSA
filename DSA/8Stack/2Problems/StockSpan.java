import java.util.ArrayDeque;
import java.util.Scanner;

public class StockSpan {
    static void printSpan(int[] prices) {
        ArrayDeque<Integer> stack = new ArrayDeque<Integer>();
        stack.push(0);
        System.out.print(1 + " ");

        for (int i = 1; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] <= prices[i]) {
                stack.pop();
            }

            System.out.print(stack.isEmpty() ? i + 1 : i - stack.peek() + " ");
            stack.push(i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int[] prices = new int[sc.nextInt()];

        System.out.print("Enter values: ");
        for (int i = 0; i < prices.length; i++) {
            prices[i] = sc.nextInt();
        }
        sc.close();
        printSpan(prices);
    }
}
