import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class S86PartitionLL {
    static Node partition(Node head, int x) {
        if (head == null || head.next == null)
            return head;

        Node node = new Node(0);
        node.next = head;

        Node back = node, front = node, temp;

        while (front.next != null) {
            if (front.next.data < x) {
                temp = front.next;
                front.next = front.next.next;

                temp.next = back.next;
                back.next = temp;
                back = back.next;
                if (back == front.next) {
                    front = front.next;
                }
                continue;
            }

            front = front.next;
        }

        return node.next;

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

        System.out.print("Enter the value of x: ");
        int x = scan.nextInt();

        System.out.print("Enter number of initial nodes: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.println("Enter value of nodes: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();
        Node head = createLinkList(arr);
        Node n_head = partition(head, x);
        printLL(n_head);
    }
}
