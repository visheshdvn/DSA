import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        next = null;
    }
}

public class LC141LinkedListCycle {

    public static boolean hasCycle(Node head) {
        if (head == null || head.next == null) {
            return false;
        }

        Node fast = head, slow = head;

        while (fast.next != null && slow.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }

            if (fast == null || slow == null) {
                return false;
            }
        }

        return false;
    }

    // creates linked
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

    // prints linkedlist
    public static void printLL(Node head) {
        if (head == null) {
            return;
        }

        System.out.print("Data: ");

        Node node = head;
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
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
        System.out.print("Linked list: ");
        printLL(head);
    }
}
