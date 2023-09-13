import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        next = null;
    }
}

public class LC24SwapNodePairs {
    static Node swapPairs(Node head) {
        if (head.next == null)
            return head;

        Node retHead = head.next;
        Node back = head, front = head.next;
        Node prev = null;

        while (front != null) {
            if (prev == null) {
                back.next = front.next;
                front.next = back;
            } else {
                prev.next = front;
                back.next = back.next.next;
                front.next = back;
            }

            if (back.next == null) {
                return retHead;
            }

            prev = back;
            back = back.next;
            front = back.next;
        }

        return retHead;
    }

    public static Node createLinkList(int arr[]) {
        if (arr.length == 0) {
            return null;
        }

        Node head = new Node(arr[0]);
        Node node = head;

        int n = 1;
        while (n < arr.length) {
            Node new_node = new Node(arr[n]);
            node.next = new_node;
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

        System.out.print("Enter value of nodes: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        scan.close();
        Node head = createLinkList(arr);
        Node n_head = swapPairs(head);
        printLL(n_head);
    }
}
