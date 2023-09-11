import java.util.List;
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
 * LC203RemoveLLElems
 */
public class LC203RemoveLLElems {

    public static ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return head;
        }

        ListNode nhead = new ListNode(-1, head);
        ListNode node = nhead;

        while (node != null && node.next != null) {
            if (node.next.val == val) {
                ListNode itr = node.next;
                while (itr != null && itr.val == val) {
                    itr = itr.next;
                }
                node.next = itr;
            }

            node = node.next;
        }

        return nhead.next;
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
        System.out.print("Enter node values: ");
        populateArr(arr, 0, n);
        
        System.out.print("Enter value to delete: ");
        int value = scan.nextInt();

        scan.close();

        ListNode head = createLL(arr);
        ListNode n_head = removeElements(head, value);
        printLL(n_head);
    }
}