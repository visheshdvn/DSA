import java.util.Scanner;

/**
 * Node
 */
class Node {
    int data;
    Node next;

    Node(int _data) {
        data = _data;
    }
}

/**
 * OddEvenLL
 */
public class OddEvenLL {
    public static Node arangeOddEven(Node head) {
        if (head.next == null) return head;

        Node oddHead = new Node(0);
        Node oddIter = oddHead;
        Node evenHead = new Node(0);
        Node evenIter = evenHead;
        Node node = head;

        while (node != null) {
            if ((node.data & 1) == 1) {
                oddIter.next = new Node(node.data);
                oddIter = oddIter.next;
            } else {
                evenIter.next = new Node(node.data);
                evenIter = evenIter.next;
            }
            node = node.next;
        }

        oddIter.next = evenHead.next;
        return oddHead.next;
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

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = scan.nextInt();
        int arr[] = new int[n];
        
        System.out.print("Enter value of nodes: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        scan.close();

        printLL(arangeOddEven(createLinkList(arr)));
    }
}