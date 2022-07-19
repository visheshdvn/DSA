
/**
 * ConstructBST
 */
import java.util.Scanner;
import java.util.Arrays;
// import javafx.util.Pair;

/**
 * Node
 */
class Node {
    int data;
    Node left;
    Node right;

    Node(int _data) {
        data = _data;
    }
}

public class ConstructBST {
    static Scanner sc;

    public static void inOrder(Node root) {
        if (root == null) {
            return;
        }

        inOrder(root.left);
        System.out.print(root.data + " ");
        inOrder(root.right);
    }

    public static int[] slice(int[] arr, int l, int r) {
        return Arrays.copyOfRange(arr, l, r);
    }

    private static Node constructBST_helper(int[] arr) {
        if (arr.length == 1) {
            return new Node(arr[0]);
        }

        if (arr.length == 0) {
            return null;
        }

        int data = arr[arr.length / 2];

        Node l_child = constructBST_helper(slice(arr, 0, arr.length / 2));
        Node r_child = constructBST_helper(slice(arr, arr.length / 2 + 1, arr.length));

        Node root = new Node(data);
        root.left = l_child;
        root.right = r_child;

        return root;

    }

    private static Node constructBST() {
        System.out.println("Enter number of nodes: ");
        int n = sc.nextInt();
        int arr[] = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        return constructBST_helper(arr);
    }

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        Node root = constructBST();
        inOrder(root);
    }
}