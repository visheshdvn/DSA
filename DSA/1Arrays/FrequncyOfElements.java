import java.util.HashMap;
import java.util.Scanner;
import java.util.Map.Entry;
import java.util.Map;

/**
 * FrequncyOfElements
 */
public class FrequncyOfElements {
    public static void frequency(int[] arr) {
        Map<Integer, Integer> m = new HashMap<>();

        for (int i : arr) {
            m.put(i, m.getOrDefault(i, 0) + 1);
        }

        for (Entry<Integer, Integer> k : m.entrySet()) {
            System.out.println(k.getKey() + " " + k.getValue());
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter length of array: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        frequency(arr);
    }
}