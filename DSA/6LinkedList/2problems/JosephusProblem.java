import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class JosephusProblem {
    static int josephus(int n, int k) {
        LinkedList<Integer> ll = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            ll.add(i);
        }

        Iterator<Integer> it = ll.iterator();
        while (ll.size() > 1) {
            int count = 0;
            while (count < k) {
                while (it.hasNext() && count < k) {
                    it.next();
                    count++;
                }
                if (count < k) {
                    it = ll.iterator();
                    it.next();
                    count++;
                }
            }
            it.remove();
        }
        return ll.getFirst();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), k = sc.nextInt();
        sc.close();

        System.out.print("Survivor: " + josephus(n, k));
    }
}
