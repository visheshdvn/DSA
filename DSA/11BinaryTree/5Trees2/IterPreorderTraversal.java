import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

class Node {
    int data;
    Node left, right;

    Node(int _data) {
        data = _data;
    }
}

public class IterPreorderTraversal {
    static Queue<Node> q = new ArrayDeque<>();

    static void insert(int data) {
        Node node = new Node(data);

        if (q.peek().left == null) {
            q.peek().left = node;
        } else if (q.peek().right == null) {
            q.peek().right = node;
            q.poll();
        }

        q.offer(node);
    }

    static Node createTree() {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = scan.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter values of nodes: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        scan.close();
        Node head = new Node(arr[0]);
        q.offer(head);

        for (int i = 1; i < n; i++) {
            insert(arr[i]);
        }

        return head;
    }

    static void preorderTraversal(Node head) {
        if (head == null) {
            return;
        }

        System.out.println(head.data);
        preorderTraversal(head.left);
        preorderTraversal(head.right);
    }

    static void iterPreorderTraversal(Node root) {
        Stack<Node> st = new Stack<>();

        Node curr = root;
        while (curr != null || st.isEmpty() == false) {

            while (curr != null) {
                System.out.println(curr.data);
                st.push(curr);
                curr = curr.left;
            }

            curr = st.pop();
            curr = curr.right;
        }
    }

    public static void main(String[] args) {
        Node head = createTree();
        preorderTraversal(head);
        System.out.println("now iter");
        iterPreorder(head);
    }
}
