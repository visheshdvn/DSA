import java.util.Scanner;

public class RopeCuttingProblem {
    public static int getNoOfPiecesHelper(int L, int a, int b, int c, int extracted, int pieces) {
        if (extracted > L) {
            return 0;
        }

        if (extracted == L) {
            return pieces;
        }

        int p1 = getNoOfPiecesHelper(L, a, b, c, extracted+a, pieces+1);
        int p2 = getNoOfPiecesHelper(L, a, b, c, extracted+b, pieces+1);
        int p3 = getNoOfPiecesHelper(L, a, b, c, extracted+c, pieces+1);

        return Math.max(Math.max(p1, p2), p3);
    }

    public static int getNoOfPieces(int L, int a, int b, int c) {
        return getNoOfPiecesHelper(L, a, b, c, 0, 0);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter length of rope: ");
        int L = Math.abs(scan.nextInt());

        System.out.print("Enter length of piece a, b, c (seperated by space or nextLine): ");
        int a = Math.abs(scan.nextInt());
        int b = Math.abs(scan.nextInt());
        int c = Math.abs(scan.nextInt());
        scan.close();

        System.out.println("The max no of pieces = " + getNoOfPieces(L, a, b, c));
    }
}
