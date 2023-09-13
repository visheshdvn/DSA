import java.util.Scanner;

public class LC50Pow {

    public static double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }

        if (n == 1) {
            return x;
        }
        double ans = 1;
        long power = (long) n;
        
        if (power < 0) {
            x = 1 / x;
            power *= -1;
        }

        while(power>0){
            if((power & 1)==1){
                ans *= x;
            }
            x *= x;
            power = power >> 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double x = scan.nextDouble();
        int n = scan.nextInt();
        scan.close();
        System.out.println(myPow(x, n));
    }
}
