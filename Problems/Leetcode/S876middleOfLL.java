import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class S876middleOfLL {
    static Node middleNode(Node head) {
        if (head.next == null)
            return head;

        Node fast = head, slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;

    }

    public static Node createLinkList(int arr[]) {
        if (arr.length == 0) {
            return null;
        }

        Node head = new Node(arr[0]);
        Node node = head;

        int n = 1;
        while (n < arr.length) {
            node.next = new Node(arr[n]);
            node = node.next;
            n += 1;
        }

        return head;
    }

    public static void printLL(Node head) {
        if (head == null) {
            return;
        }

        Node node = head;
        while (node != null) {
            System.out.println("Data: " + node.data);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of initial nodes: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.println("Enter value of nodes: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();
        Node head = createLinkList(arr);
        // printLL(head);
        Node n_head = middleNode(head);
        System.out.print(n_head.data);
    }
}
