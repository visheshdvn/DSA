
import java.util.Scanner;;

public class UserInput {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int i = scan.nextInt();
        int j = scan.nextInt();
        scan.close();
        
        System.out.println(i + j);
    }
}
