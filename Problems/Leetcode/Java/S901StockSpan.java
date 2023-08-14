import java.util.ArrayDeque;
import java.util.Scanner;

class StockSpanner {
    public class Pair {
        int day, value;

        Pair(int _day, int _value) {
            day = _day;
            value = _value;
        }
    }

    ArrayDeque<Pair> stack;
    int curr_day = -1;

    public StockSpanner() {
        stack = new ArrayDeque<Pair>();
    }

    public int next(int price) {
        curr_day++;
        if (curr_day == 0) {
            stack.push(new Pair(curr_day, price));
            return 1;
        }

        while (!stack.isEmpty() && stack.peek().value <= price) {
            stack.pop();
        }

        int span = stack.isEmpty() ? curr_day + 1 : curr_day - stack.peek().day;
        stack.push(new Pair(curr_day, price));
        return span;
    }
}

public class S901StockSpan {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int[] prices = new int[sc.nextInt()];

        System.out.print("Enter values: ");
        for (int i = 0; i < prices.length; i++) {
            prices[i] = sc.nextInt();
        }
        sc.close();

        StockSpanner obj = new StockSpanner();
        for (int i = 0; i < prices.length; i++) {
            System.out.println(obj.next(prices[i]));
        }
    }
}
