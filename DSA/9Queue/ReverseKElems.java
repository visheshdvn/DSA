import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class ReverseKElems {
    static void reverseKElems(Queue<Integer> q, int k) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int n = q.size();

        for (int i = 0; i < k; i++) {
            stack.push(q.poll());
        }

        while (!stack.isEmpty()) {
            q.offer(stack.pop());
        }

        for (int i = 0; i < n - k; i++) {
            q.offer(q.poll());
        }
    }

    static void printElementsOfQ(Queue<Integer> q) {
        while (!q.isEmpty()) {
            System.out.print(q.poll() + " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new ArrayDeque<Integer>();

        System.out.print("Enter number of elements in queue: ");
        int n = sc.nextInt();

        System.out.print("Enter values: ");
        for (int i = 0; i < n; i++) {
            q.offer(sc.nextInt());
        }

        System.out.print("Enter value of K: ");
        int k = sc.nextInt();
        sc.close();

        reverseKElems(q, k);
        printElementsOfQ(q);
    }
}
