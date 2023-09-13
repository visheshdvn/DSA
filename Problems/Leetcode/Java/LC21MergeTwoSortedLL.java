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

public class LC21MergeTwoSortedLL {
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(-1);
        ListNode node = head;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                node.next = list1;
                list1 = list1.next;
                node = node.next;
            } else {
                node.next = list2;
                list2 = list2.next;
                node = node.next;
            }
        }

        while (list1 != null) {
            node.next = list1;
            list1 = list1.next;
            node = node.next;
        }

        while (list2 != null) {
            node.next = list2;
            list2 = list2.next;
            node = node.next;
        }

        return head.next;
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

        // create LL1
        System.out.print("Enter number of nodes in list 1: ");
        int m = scan.nextInt();
        int arr[] = new int[m];
        System.out.print("Enter node data: ");
        populateArr(arr, 0, m);

        // create LL1
        System.out.print("Enter number of nodes in list 2: ");
        int n = scan.nextInt();
        int arr2[] = new int[n];
        System.out.print("Enter node data: ");
        populateArr(arr2, 0, n);

        scan.close();

        ListNode head = createLL(arr);
        ListNode head2 = createLL(arr2);
        ListNode n_head = mergeTwoLists(head, head2);
        printLL(n_head);
    }
}
