import java.util.Scanner;

public class DecimalToBinary {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

        String binaryStr = "";
        while (n > 0) {
            binaryStr = (n & 1) + binaryStr;
            n = n >> 1;
        }

        System.out.println(binaryStr);
    }
}
