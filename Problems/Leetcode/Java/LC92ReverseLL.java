import java.util.Scanner;

class ListNode {
    int data;
    ListNode next;

    ListNode(int _data) {
        data = _data;
    }

    ListNode(int _data, ListNode _node) {
        data = _data;
        next = _node;
    }
}

/**
 * S92ReverseLL
 */
public class LC92ReverseLL {

    public static ListNode reverseLL(ListNode head, int left, int right) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode back = null;
        ListNode node = head;

        while (left > 1) {
            back = node;
            node = node.next;
            left--;
            right--;
        }

        ListNode connection = back;
        ListNode tail = node;

        while (right > 0) {
            ListNode front = node.next;
            node.next = back;
            back = node;
            node = front;
            right--;
        }

        if (connection != null) {
            connection.next = back;
        } else {
            head = back;
        }

        tail.next = node;
        return head;
    }

    public static ListNode createLL(int arr[]) {
        ListNode head = new ListNode(arr[0]);
        ListNode node = head;

        for (int i = 1; i < arr.length; i++) {
            ListNode new_node = new ListNode(arr[i]);
            node.next = new_node;
            node = node.next;
        }

        return head;
    }

    public static void printLL(ListNode head) {
        ListNode node = head;
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = scan.nextInt();

        int arr[] = new int[n];
        System.out.print("Enter node data: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }

        System.out.print("Enter left and right index: ");
        int left = scan.nextInt();
        int right = scan.nextInt();
        scan.close();

        ListNode head = createLL(arr);
        ListNode n_head = reverseLL(head, left, right);
        printLL(n_head);
    }
}