import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LC412FizzBuzz {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

        List<String> arr = new ArrayList<>();

        for (int i = 1; i < n + 1; i++) {
            arr.add(String.valueOf(i));
        }

        for (int i = 2; i < n + 1; i += 3) {
            if (i >= arr.size())
                break;
            arr.set(i, "Fizz");
        }

        for (int i = 4; i < n + 1; i += 5) {
            if (i >= arr.size())
                break;
            arr.set(i, "Buzz");
        }

        for (int i = 14; i < n + 1; i += 15) {
            if (i >= arr.size())
                break;
            arr.set(i, "FizzBuzz");
        }

        for (String i : arr) {
            System.out.println(i);
        }
    }
}
