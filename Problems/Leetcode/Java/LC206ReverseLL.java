import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

/**
 * LC206ReverseLL
 */
public class LC206ReverseLL {
    public static ListNode reverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode back = null, mid = head, front = head.next;

        while (front != null) {
            mid.next = back;
            back = mid;
            mid = front;
            front = front.next;
        }

        mid.next = back;

        return mid;
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
            System.out.print(node.val + " ");
            node = node.next;
        }
    }

    public static void populateArr(int[] arr, int startIndex, int n) {
        // populates n numbers from startIndex
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < startIndex + n; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = scan.nextInt();

        int arr[] = new int[n];
        System.out.print("Enter node data: ");
        populateArr(arr, 0, n);

        scan.close();

        ListNode head = createLL(arr);
        ListNode n_head = reverseList(head);
        printLL(n_head);
    }
}